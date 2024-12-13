from django.db import models

class News(models.Model):
    '''Новости и записи'''
    title = models.CharField('Заголовок записи', max_length=250)
    annotation = models.TextField('Аннотация')
    description = models.TextField('Текст записи')
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y', blank=True, null=True)
    video = models.FileField('Видео', upload_to='video/%Y', blank=True, null=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f"{self.title}, {self.author}, {self.date}"


class Comments(models.Model):
    '''Комментарии'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comment = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(News, verbose_name="Публикация", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f"{self.name}, {self.post}"





