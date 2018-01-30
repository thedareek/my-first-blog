from django.db import models




class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > 1000:
            return self.text[:1000]
        else:
            return self.text