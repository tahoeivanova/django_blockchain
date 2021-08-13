from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import os
import hashlib
import json
import os
import os.path as osp
from django.core.files.base import ContentFile, File


# Create your models here.
class Block(models.Model):
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    to_whom = models.CharField(max_length=256)
    prev_hash = models.CharField(max_length=256, default='')
    info = models.BinaryField(null=True)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id} {self.name} {self.amount} {self.to_whom} {self.prev_hash}'

    def save(self, *args, **kwargs):
        try:
            self.prev_hash = self.get_hash_from_previous(*args)


        except Exception as e:
            print(e)

        super(Block, self).save(*args, **kwargs)


    def get_hash_from_previous(self, *args):
        last_block = Block.objects.last()
        info = last_block.infofile.info
        hash_for_data = hashlib.md5(info).hexdigest()
        return hash_for_data


class Infofile(models.Model):
    info = models.BinaryField(null=True)
    created_at = models.DateTimeField('created at', null=True, blank=True)
    block = models.OneToOneField(Block, on_delete=models.CASCADE, related_name='infofile')



    def __str__(self):
        return f'{type(self.info)}'

@receiver(post_save, sender=Block)
def create_info(sender, instance, **kwargs):
    info = {'name': instance.name,
            'amount': instance.amount,
            'to_whom': instance.to_whom,
            'hash': instance.prev_hash}
    # with open(f'{Block.id}') as f:
    #     json.dump(info, f, ensure_ascii=False, indent=4)
    filename = str(instance.id)
    with open(osp.join('uploads', filename), 'w') as f:
        json.dump(info, f, ensure_ascii=False, indent=4)

        # task.uploads.save(f'{Block.id}', File(f))
    file = open(osp.join('uploads', filename), 'rb').read()
    Infofile.objects.create(block=instance, info=file)






