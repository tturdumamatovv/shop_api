from django.db import models
from django.contrib.auth import get_user_model


from product.models import Product


User = get_user_model()


class Mark():
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    marks = (
        (one, 'Too bad!'),
        (two, 'Bad!'),
        (three, 'Normal!'),
        (four, 'Good!'),
        (five, 'Excellent!'),
    )

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField(choices=Mark.marks)
    created_at = models.DateTimeField(auto_now_add=True)

