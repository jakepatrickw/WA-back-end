import uuid
from django.db import models
from django.contrib.auth.models import User

def create_unique_filename(filename):
    extension = filename.split('.')[-1]
    return str(uuid.uuid4()) + '.' + extension 

def user_directory_path(instance, filename):
    unique_name = create_unique_filename(filename)
    return 'files/user_{0}/user_image/{1}'.format(instance.user_id.id, unique_name)

class UserImage(models.Model):
    picture = models.FileField(upload_to = user_directory_path)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

