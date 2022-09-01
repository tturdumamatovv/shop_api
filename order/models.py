from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver


from account.send_email import send_notifications
from product.models import Product


User = get_user_model()

STATUS_CHOICES = (
    ('Open', 'Открыт'),
    ('In_process', 'В обработке'),
    ('Closed', 'Закрыт')
)

class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)




class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.RESTRICT)
    product = models.ManyToManyField(Product, through=OrderItem)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}'


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, *args, **kwargs):
    send_notifications(instance.user, instance.id)
