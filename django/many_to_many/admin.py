from django.contrib import admin
# Register your models here.

from .models import (
    # basic
    Topping, Pizza,
    # intermediate
    Post, User, PostLike,
    # self
    FacebookUser,
    # symmetrical
    symmetrical
    )

admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
admin.site.register(FacebookUser)
# admin.site.register(symmetrical)