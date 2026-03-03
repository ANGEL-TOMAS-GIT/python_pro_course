from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    slug = models.SlugField(unique=True, max_length=40, verbose_name="Slug")
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name="Book Title")
    book_author = models.CharField(max_length=20, verbose_name="Book author", blank=True)
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
    
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.title}({self.published_at}) - {self.author}'
    
    @property
    def is_on_market(self) -> bool:
        return all([self.is_available, self.author])
