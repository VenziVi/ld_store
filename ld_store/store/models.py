from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    featured_products = models.ForeignKey('Product',
                                          on_delete=models.SET_NULL,
                                          null=True,
                                          related_name='+')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un_branded')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.1), MaxValueValidator(500)])
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])