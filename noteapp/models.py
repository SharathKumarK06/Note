from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    @classmethod
    def get_default_pk(cls):
        default_category = cls.objects.get_or_create(name="Uncategorized")
        return default_category.pk

class Note(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank=False)
    last_modified = models.DateTimeField(auto_now=True, blank=False)
    categories = models.ManyToManyField("Category",
                                        default=Category.get_default_pk,
                                        related_name="notes")
