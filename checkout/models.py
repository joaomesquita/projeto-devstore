from django.db import models
from django.conf import settings
from django.db.models import Sum
from pagseguro import PagSeguro

from catalog.models import Product, Size

# Create your models here.
class CartItemManager(models.Manager):

    def add_item(self, cart_key, product, value_size):
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity + 1
            print(cart_item.quantity)
            cart_item.save()
        else:
            created = True
            if product.sale:
                cart_item = CartItem.objects.create(cart_key=cart_key, product=product, price=product.sale, size=value_size)
            else:
                cart_item = CartItem.objects.create(cart_key=cart_key, product=product, price=product.price, size=value_size)
        return cart_item, created

class CartItem(models.Model):

    cart_key = models.CharField('Chave do Carrinho', max_length=40, db_index=True)
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    size = models.CharField('Tamanho', max_length=3, null=True)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key', 'product'),)

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)

class OrderManager(models.Manager):

    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order, quantity=cart_item.quantity, product=cart_item.product, price=cart_item.price, size=cart_item.size
            )
        return order

class Order(models.Model):
    
    STATUS_CHOICES = (
        (1, 'Aguardando pagamento'),
        (2, 'Em análise'),
        (3, 'Paga'),
        (4, 'Disponível'),
        (5, 'Em disputa'),
        (6, 'Devolvida'),
        (7, 'Cancelada'),
    )
    PAYMENT_OPTION_CHOICES = (
        ('pagseguro', 'PagSeguro'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE)
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=1, blank=True)
    payment_option = models.CharField('Opção de Pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=20, default='pagseguro')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)

    def products(self):
        products_ids = self.items.values_list('product')
        return Product.objects.filter(pk__in=products_ids)

    def sub_total(self):
        aggregate_queryset = self.items.aggregate(
            sub_total=models.Sum(
                models.F('price') * models.F('quantity'), output_field=models.DecimalField()
            )
        )
        return aggregate_queryset['sub_total']

    def total(self):
        aggregate_queryset = self.items.aggregate(
            total=models.Sum(
                models.F('price') * models.F('quantity'), output_field=models.DecimalField()
            )
        )
        return aggregate_queryset['total']

    def pagseguro_update_status(self, status):
        if status == '1':
            self.status = 1
        elif status == '2':
            self.status = 2
        elif status == '3':
            self.status = 3
        elif status == '4':
            self.status = 4
        elif status == '5':
            self.status = 5
        elif status == '6':
            self.status = 6
        elif status == '7':
            self.status = 7
        self.save()

    def pagseguro(self):
        self.payment_option = 'pagseguro'
        self.save()
        if settings.PAGSEGURO_SANDBOX:
            pg = PagSeguro(
                email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
                config={'sandbox': settings.PAGSEGURO_SANDBOX}
            )
        else:
            pg = PagSeguro(
                email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN
            )
        pg.sender = {
            'email': self.user.email
        }
        pg.reference_prefix = None
        pg.shipping = None
        pg.reference = self.pk
        for item in self.items.all():
            pg.items.append(
                {
                    'id': item.product.pk,
                    'description': item.product.name,
                    'quantity': item.quantity,
                    'amount': '%.2f' % item.price
                }
            )
        return pg

class OrderItem(models.Model):

    order = models.ForeignKey(Order, verbose_name='Pedido', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    size = models.CharField('Tamanho', max_length=3, null=True)

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens dos Pedidos'

    def __str__(self):
        return '[{}] {}'.format(self.order, self.product)

def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()

models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)
