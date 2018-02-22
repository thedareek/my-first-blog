from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d', help_text='150x150px',
                              verbose_name='Ссылка картинки')

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > 990:
            return self.text[:990]
        else:
            return self.text


class Comments(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    comments_author = models.CharField(max_length=100)
    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_date = models.DateTimeField(auto_now_add=True)
    comments_article = models.ForeignKey('Article', on_delete=models.CASCADE)
