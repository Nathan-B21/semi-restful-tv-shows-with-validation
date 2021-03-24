from django.db import models
from datetime import datetime


class ShowManager(models.Manager):
    def showValidator(self, postData):
        day = datetime.now().strftime("%Y-%m-%d")
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be longer than two characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network must be longer than three characters"
        # if day:
        #     errors['releasedate'] = "Release date must be longer than two characters"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description must be longer than 9 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
