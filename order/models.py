from django.db import models
from product.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, null=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class Order(models.Model):
    customer_name = models.CharField(max_length=100, null=True)
    customer_email = models.EmailField(max_length=120, null=True)
    customer_phone = models.CharField(max_length=48, null=False)
    customer_address = models.TextField(null=False)
    comment = models.TextField(null=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=False)
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.cost_per_item = self.product.price
        self.total_cost = self.quantity * self.cost_per_item
        return super(OrderProducts, self).save()

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'


@receiver(post_save, sender=OrderProducts)
def model_post_save(sender, **kwargs):
    order = kwargs['instance'].order
    all_order_products = sender.objects.filter(order=order)
    order_total_price = 0

    for item in all_order_products:
        order_total_price += item.total_cost

    order.amount = order_total_price
    order.save(force_update=True)
