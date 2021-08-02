from django.db import models
class Article(models.Model):
    title=models.CharField("Название", max_length=200,default='Пошел на хуй') #создаю поле на ограниченное число символов
    anons=models.CharField("Анонс", max_length=200,default='Пошел на хуй')
    full_text=models.TextField("Статья")#создаем поле с большим кол-вом симоволов
    date=models.DateTimeField("Дата и время публикации")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name='Новость'
        verbose_name_plural = 'Новости'

# Create your models here.
