from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey('Group', blank=True, null=True,
                              on_delete=models.CASCADE)


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=False,
                            verbose_name="URL")
    description = models.TextField(max_length=700, blank=True)

    def __str__(self) -> str:
        return self.title
