from django.db import models
from django.conf import settings
from profiles_api import models as profiles_models

import datetime


# Create your models here.


class PostCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    """Post to be used for a recipe"""
    title = models.CharField(max_length=255)
    post_category = models.OneToOneField(
        PostCategory, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class PostTag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.OneToOneField(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_id.title


class PostImages(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PostComment(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.message


class PostBookmark(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.post_id.title


class ReportCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class PostReport(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.OneToOneField(ReportCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.post_id.title


class CommentReport(models.Model):
    user_id = models.ForeignKey(
        profiles_models.UserProfile, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    category = models.OneToOneField(ReportCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.comment_id.message
