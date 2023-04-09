from shortuuid.django_fields import ShortUUIDField 
from apps.common.models import TimeStampedUUIDModel
from django.db import models

class Tag(TimeStampedUUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class TagModule(TimeStampedUUIDModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    module = models.ForeignKey('Module', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tag.name} - {self.module.name}"
    

class Module(TimeStampedUUIDModel):
    name = models.CharField(max_length=200)
    course_id = models.UUIDField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    tags = models.ManyToManyField(Tag, through='TagModule')

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['course_id']),
            models.Index(fields=['created_at']),
        ]
        ordering = ['name']
