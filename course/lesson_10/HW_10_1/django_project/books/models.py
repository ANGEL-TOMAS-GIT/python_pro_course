from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

User = get_user_model()


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    slug = models.SlugField(unique=True, max_length=40, verbose_name="Slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Description(models.Model):
    text = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.text[:50]


class Book(models.Model):
    title = models.CharField(max_length=30, verbose_name="Book Title")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_at = models.DateField(verbose_name='release date')
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="books",
        null=True,
        blank=True
    )

    description = models.ForeignKey(
        Description,
        related_name="books",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return f'{self.title}({self.published_at}) - {self.author}'

    @property
    def is_on_market(self) -> bool:
        return all([self.is_available, self.author])
