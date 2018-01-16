from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class PinImage(models.Model):
    uuid = models.CharField(max_length=10, blank=True, unique=True)
    slug = models.SlugField(max_length=200, blank=True, unique=False)
    image = models.FileField(upload_to='pinImages/') # /images/upload/4904712826.jpg
    note = models.TextField(max_length=500)
    published = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.uuid

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.id))
            super(PinImage, self).save(*args, **kwargs)
        else:
            super(PinImage, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, blank=True, unique=False)
    images = models.ManyToManyField(PinImage, through='ImageHasCategory') # category.images.all()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Category, self).save(*args, **kwargs)
        else:
            super(Category, self).save(*args, **kwargs)


class ImageHasCategory(models.Model):
    pinImage = models.ForeignKey(PinImage, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    class Meta:
        unique_together = ['pinImage', 'category']
        verbose_name_plural = 'pinImage has categories'

    def __str__(self):
        return str(self.pinImage.uuid)

