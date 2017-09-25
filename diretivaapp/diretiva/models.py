from django.db import models


class Diretiva(models.Model):
    # https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.DateField
    date_entry = models.DateTimeField()  # em prod usar o auto_now_add
    status = models.BooleanField(blank=False, default=False)
    main_ticket = models.IntegerField(blank=False)
    product = models.CharField(blank=False, max_length=30)
    description = models.TextField(blank=False)
    # https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.DateField
    date_update = models.DateTimeField()  # em prod usar o auto_now
    date_closed = models.DateTimeField(null=True)



