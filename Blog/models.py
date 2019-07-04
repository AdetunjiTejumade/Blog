from django.db import models
from django.utils import timezone
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date_published = models.DateTimeField()

    def get_absolute_url(self):
        return f"/{self.id}/"

    class Meta:
        ordering = ['-date_published',]

class Comment(models.Model):
    post = models.ForeignKey('Blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    add_name = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text