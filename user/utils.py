from django.conf import settings
import os


def upload_location(instance, filename):
    file_path = 'profile/user_{user_id}/post.jpeg'.format(
        user_id=str(instance.user.id), filename=filename
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path