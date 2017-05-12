from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    trans_hash = models.CharField(max_length=512, null=False, blank=False)
    trans_type = models.CharField(max_length=512, null=False, blank=False)
    trans_from = models.CharField(max_length=512, null=False, blank=False)
    trans_status = models.BooleanField(default=False)
    # block_number = models.IntegerField(default=0, null=False)
    #friends = models.CharField(max_length=512)
    class Meta:
        db_table = u"transaction"