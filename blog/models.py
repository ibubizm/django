from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=200, db_index=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'pip': self.pk})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'pip': self.pk})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'pip': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
