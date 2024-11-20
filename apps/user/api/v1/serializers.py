from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Fields:
        email (str): The email of the user. Required.
        password (str): The password of the user. Write-only and required.
        first_name (str): The first name of the user. Optional.
        last_name (str): The last name of the user. Optional.
        team (str): The team of the user. Optional.

    Methods:
        create(validated_data):
            Creates a new user instance with the provided validated data.
    """

    password_confirm = serializers.CharField(write_only=True, required=True)
    access = serializers.CharField(read_only=True, required=False)
    refresh = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            "password_confirm",
            'first_name',
            'last_name',
            'team',
            'access',
            'refresh'
        )

        extra_kwargs = {
            'id': {'read_only': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'password_confirm': {'write_only': True, 'required': True},
            'team': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate(self, attrs):
        """
        Validate the serializer data to ensure the passwords match.

        Parameters:
            attrs (dict): A dictionary containing the validated data passed to the serializer.

        Returns:
            dict: The same `attrs` dictionary if validation passes successfully.

        Raises:
            serializers.ValidationError: If the `password` and `password_confirm` fields
                                         do not have the same value.
        """
        if 'password' in attrs and 'password_confirm' in attrs:
            if attrs['password'] != attrs['password_confirm']:
                raise serializers.ValidationError({"password": "Passwords must match."})

            # Minimum password length check for security
            if len(attrs['password']) < 8:
                raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})

            # Check for common weak passwords
            weak_passwords = ['password', '123456', 'qwerty']
            if attrs['password'] in weak_passwords:
                raise serializers.ValidationError({"password": "Password is too weak. Choose a stronger password."})

        if 'email' in attrs:
            if User.objects.filter(email=attrs['email']).exists():
                raise serializers.ValidationError({"email": "A user with that email already exists."})

        return attrs

    def create(self, validated_data):
        """
        Create a new user instance.

        Args:
            validated_data (dict): The validated data from the serializer.

        Returns:
            User: The created user instance.
        """
        try:
            password = validated_data.pop('password')
            validated_data['username'] = validated_data['email']
            validated_data.pop('password_confirm')

            # Create the user instance
            user = User(**validated_data)
            user.set_password(password)
            user.save()

            return user

        except Exception as e:
            raise serializers.ValidationError({"error": "User creation failed due to an unexpected error."})

    def update(self, instance, validated_data):
        """
        Update the user instance with the provided validated data.

        Args:
            instance (User): The user instance to update.
            validated_data (dict): The validated data from the serializer.

        Returns:
            User: The updated user instance.
        """

        update_fields = list(validated_data.keys())

        # Update email
        if 'email' in validated_data:
            instance.email = validated_data['email']
            instance.username = validated_data['email']
            update_fields.append('username')

        # Update first name
        if 'first_name' in validated_data:
            instance.first_name = validated_data['first_name']

        # Update last name
        if 'last_name' in validated_data:
            instance.last_name = validated_data['last_name']

        # Update password
        if 'password' in validated_data:
            update_fields.remove("password_confirm")
            instance.set_password(validated_data['password'])

        # Update team
        if 'team' in validated_data:
            instance.team = validated_data['team']

        instance.save(update_fields=update_fields)

        return instance

    def to_representation(self, instance):
        """
        Customize the data representation.

        Only include `access` and `refresh` tokens in the response during the `create` action.
        """
        representation = super().to_representation(instance)

        # Include tokens only during the create action
        if self.context.get('view').action == 'create':
            refresh = RefreshToken.for_user(instance)
            representation['access'] = str(refresh.access_token)
            representation['refresh'] = str(refresh)

        return representation
