from secretsantasu.apps.userprofile.models import UserProfile


def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
