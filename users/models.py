from django.db import models
from django.contrib.auth.models import User

from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True,default='Awesome bio!')
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self):
        super().save()

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

