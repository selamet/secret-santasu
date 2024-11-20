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
        company (str): The company of the user. Required.

    Methods:
        create(validated_data):
            Creates a new user instance with the provided validated data.
    """

    password_confirm = serializers.CharField(write_only=True, required=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', "password_confirm", 'first_name', 'last_name', 'company', "access", "refresh")
        extra_kwargs = {
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'password_confirm': {'write_only': True, 'required': True},
            'company': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'access': {'read_only': True},
            'refresh': {'read_only': True},
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
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords must match."})

        # Minimum password length check for security
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters long."})

        # Check for common weak passwords
        weak_passwords = ['password', '123456', 'qwerty']
        if attrs['password'] in weak_passwords:
            raise serializers.ValidationError({"password": "Password is too weak. Choose a stronger password."})

        return attrs

    def validate_email(self, value):
        """
        Validate the email field to ensure it is unique.

        Parameters:
            value (str): The email value to validate.

        Returns:
            str: The same email value if validation passes successfully.

        Raises:
            serializers.ValidationError: If a user with the same email already exists.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")

        return value

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

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            user.access = str(access)
            user.refresh = str(refresh)

            return user

        except Exception as e:
            raise serializers.ValidationError({"error": "User creation failed due to an unexpected error."})
