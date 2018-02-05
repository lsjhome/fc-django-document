from datetime import datetime
from django.utils import timezone

from django.db import models


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

# Extra fields on many-to-many relationships


class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        # MTM으로 연결된 반대편에서
        # (지금의 경우 특정 User가 좋아요 누른
        #   Post목록을 가져오고 싶은 경우)
        #
        related_name='like_posts',
    )

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def __str__(self):
        # 글 title이 "공지사항" 이며
        # 유저 name이 "이한영"이고,
        # 좋아요 누른 사람이 2018.01.31 일때
        # "공지사항"글의 좋아요(이한영, 2018.01.31)으로 출력
        return '"{title}"글의 좋아요({name}, {date})'.format(
            title = self.post.title,
            name = self.user.name,
            date = datetime.strtime(
                timezone.make_naive(self.created_date),
                '%Y.%m.%d'),
            )
