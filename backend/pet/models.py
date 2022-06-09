from django.db import models

# Create your models here.
class Base(models.Model):
    online = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Pet(Base):
    nome = models.CharField(blank=False, null=False, max_length=50)
    historia = models.TextField(blank=False, null=False)
    foto = models.URLField(blank=False, null=False)

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"

    def __str__(self):
        return self.nome
