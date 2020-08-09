from django.db import models

from django.db import models
from django.utils import timezone

category_choices = (
    ('fashion', 'FASHION'),
    ('beauty', 'BEAUTY'),
    ('art', 'ART')
)

class MagazinePosts(models.Model):
    image = models.ImageField(upload_to='magazine_pics', null=True, blank=True)
    title = models.CharField(max_length=100)
    article = models.TextField()
    category = models.CharField(max_length=50, choices=category_choices, default='fashion')
    date_posted = models.DateTimeField(default=timezone.now)

