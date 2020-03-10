from django.db import models

# Create your models here.


class ImageModel(models.Model):
    image = models.ImageField(upload_to="media/")
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=200)
    image_comments = models.CharField(max_length=300)
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_caption


class ProfileModel(models.Model):
    profile_pic = models.ImageField(upload_to="media/")
    profile_username = models.CharField(max_length=30)
    profile_userpassword = models.CharField(max_length=20)
    profile_bio = models.CharField(max_length=400)

    def __str__(self):
        return self.profile_username


"""
image model methods
"""

## save_image
@classmethod
def save_image(cls=ImageModel):
    pass


## delete_method
@classmethod
def delete_image(cls=ImageModel):
    pass


## update_caption
@classmethod
def update_caption(cls=ImageModel):
    pass
