from django.db import models
from django.utils.translation import gettext_lazy as _

from ikwen.core.models import Model
from ikwen.core.fields import FileField


class Gallery(Model):
    IMAGE_UPLOAD_TO = 'Gallery'
    media = FileField(blank=True, null=True, allowed_extensions=['jpg', 'jpeg', 'png', 'heic', 'mp4', 'avi', 'webm', 'mov', 'ogg', 'wmv'],
                      upload_to=IMAGE_UPLOAD_TO, help_text=_("Upload a single media file here"))
    name = models.CharField(_('Image name'), max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Partner(Model):
    IMAGE_UPLOAD_TO = 'Gallery'
    logo = FileField(blank=True, null=True, allowed_extensions=['jpg', 'jpeg', 'png', 'heic'],
                      upload_to=IMAGE_UPLOAD_TO, help_text=_("Upload a single logo file here"))
    name = models.CharField(_('Image name'), max_length=250, blank=True, null=True)

    def __unicode__(self):
        return self.name



