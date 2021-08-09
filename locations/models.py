from helpers.models import Timestamps
from django.contrib.gis.db import models


class Location(Timestamps):
    location = models.PointField(default=None)
    address_info = models.TextField()
    city = models.ForeignKey('branches.City', on_delete=models.CASCADE, default=1)
