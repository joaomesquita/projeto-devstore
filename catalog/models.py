from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria', on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    sale = models.DecimalField('Preço Promocional', decimal_places=2, max_digits=8, null=True, blank=True)
    quantity = models.IntegerField('Quantidade', null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})

class ProductVariation(models.Model):
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', on_delete=models.CASCADE)
    size = models.CharField('Tamanho', max_length=3, null=True, blank=True)

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

    def __str__(self):
        return self.product.name

class ProductImage(models.Model):
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', on_delete=models.CASCADE)
    image = CloudinaryField('Imagem', null=True, blank=True)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return self.product.name

