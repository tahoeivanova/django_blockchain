from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import os
import hashlib


# Create your models here.
class Block(models.Model):
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    to_whom = models.CharField(max_length=256)
    prev_hash = models.CharField(max_length=256, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id} {self.name} {self.amount} {self.to_whom} {self.prev_hash}'

    def save(self, *args, **kwargs):
        try:
            self.prev_hash = self.get_hash_from_previous(*args)
        except:
            pass

        super(Block, self).save(*args, **kwargs)


    def get_hash_from_previous(self, *args):
        # data = open(args, 'rb').read()
        last_str = Block.objects.last()
        info = last_str.name
        hash_for_data = hashlib.md5(info.encode('utf-8')).hexdigest()
        return hash_for_data


class Infofile(models.Model):
    info = models.TextField(blank=True)
    block = models.OneToOneField(Block, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.block}'

@receiver(post_save, sender=Block)
def create_info(sender, instance, **kwargs):
    Infofile.objects.create(block=instance, info='some info')





