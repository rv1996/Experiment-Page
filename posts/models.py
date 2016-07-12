from __future__ import unicode_literals
from django.db.models.signals import pre_save
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify


# Create your models here.

def upload_to(instance, filename):
    return "{}/{}".format(instance.id, filename)


class Experiment(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to=upload_to, height_field="height_field",
                              width_field="width_field")
    slug = models.SlugField(unique=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # for python 3 use __unicode__(self)
    def __str__(self):
        return "Name = {}".format(self.title)

    def get_absolute_url(self):
        return reverse("posts:detail_view", kwargs={'slug': self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    qs = Experiment.objects.filter(slug=slug).order_by("-id")
    exist = qs.exists()
    if exist:
        new_slug = "%S-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)

    return slug

def pre_save_post_signal_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_signal_receiver, sender=Experiment)
