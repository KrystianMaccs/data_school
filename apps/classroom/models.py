from django.db import models
from apps.common.models import TimeStampedUUIDModel


class RoomMember(TimeStampedUUIDModel):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name
