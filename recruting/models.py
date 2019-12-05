from django.db import models
from django.urls import reverse

a_choices = (
        (True, 'Да'),
        (False, 'Нет')
    )


class Planet(models.Model):
    name = models.CharField(verbose_name="Название планеты", unique=True, max_length=255)

    def __str__(self):
        return self.name


class Recruit(models.Model):
    name = models.CharField(verbose_name="Имя рекрута", max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.SET_NULL, verbose_name="Планета обитания", null=True)
    age = models.PositiveIntegerField(verbose_name="Возраст")
    email = models.EmailField(verbose_name="Почтовый адрес", unique=True)
    shadow = models.BooleanField(default=False, choices=a_choices, verbose_name="Является рукой тени?")
    master = models.ForeignKey('Sith', on_delete=models.CASCADE, blank=True, null=True, related_name='recruit')

    def __str__(self):
        return f'Рекрут: {self.name} - {self.planet}'

    def get_absolute_url(self):
        return reverse('recruit_page', args=[self.pk])


class Sith(models.Model):
    name = models.CharField(verbose_name="Имя ситха", max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.SET_NULL, verbose_name="Планета преподования", null=True)

    def __str__(self):
        return f'Ситх: {self.name} -  {self.planet}'


class Question(models.Model):
    unique_code = models.CharField(unique=True, max_length=15, verbose_name="Уникальный код")
    text = models.TextField(verbose_name="Вопрос", max_length=500)

    def __str__(self):
        return self.unique_code


class Answer(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, verbose_name="Рекрут")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Тест")
    answer = models.BooleanField(default=False, choices=a_choices, verbose_name='Ответ на вопрос')

    def __str__(self):
        return f'{self.question} - {self.answer}'



