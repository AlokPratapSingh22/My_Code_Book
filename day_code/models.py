from django.db import models
from django.db.models.fields import NullBooleanField
from django.utils import timezone
from django.urls import reverse


class CodeBlock(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("day_code:block_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class CodePage(models.Model):
    code_block = models.ForeignKey(
        'CodeBlock', related_name='pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    question = models.TextField(null=False)
    code = models.TextField(null=True)
    create_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        _ = self.pk
        return reverse("day_code:block_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
