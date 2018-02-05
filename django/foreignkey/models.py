from django.db import models

# verbose_name지정
# admin에 등록
# migration생성 및 적용


class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer', # 이렇게 문자열 처리를 해 두면 아래의 클래스를 알아서 찾는다.
        on_delete=models.CASCADE,
        verbose_name='제조사',
    )
    name = models.CharField('모델명', max_length=60)

    def __str__(self):
        # 현대 아반테 <- 와 같이 출력되도록 처리
        return f'{self.manufacturer.name} {self.name}'


class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=60)
    # 자기 자신을 다대일로 연결하느 필드
    # 비어있어도 무관, 연결된 객체가 삭제되면 함께 삭제되지 않고
    # 해당 필트를 비움
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Type(models.Model):
    type_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.type_number}| {self.name}'


class Pokemon(models.Model):
    dex_number = models.IntegerField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dex_number:03}. {self.name} ({self.type.name})'

