from django.db import models

# Create your models here.


class Profile(models.Model):
    profile_dp = models.ImageField(upload_to="media/")
    profile_name = models.CharField(max_length=30)
    profile_password = models.CharField(max_length=20)
    profile_biography = models.CharField(max_length=400)

    def __str__(self):
        return self.profile_username


class Image(models.Model):
    image = models.ImageField(upload_to="media/")
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=200)
    image_comments = models.CharField(max_length=300)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_caption


"""
image model methods
"""

## save_image
@classmethod
def save_image(cls=Image):
    pass


## delete_method
@classmethod
def delete_image(cls=Image):
    pass


## update_caption
@classmethod
def update_caption(cls=Image):
    pass
