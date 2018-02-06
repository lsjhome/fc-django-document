from django.db import models


__all__ = ('Topping', 'Pizza')


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    # ...
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping) # 다대 다라도 이게 중심에 되는게 맞으니 이쪽에 이렇게 넣어준다.

    def __str__(self):
        return self.name


