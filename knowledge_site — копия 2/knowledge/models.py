from django.db import models

class KnowledgeField(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=2500)  # Название статьи
    link = models.URLField(max_length=2500, null=True, blank=True, default="Ссылка отсутствует")  # Ссылка
    doi = models.CharField(max_length=2500, null=True, blank=True)  # DOI
    author = models.CharField(max_length=2500, null=True, blank=True, default="Автор отсутствует")
    field = models.ForeignKey(KnowledgeField, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title

class GaluzNauki(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Назва галузі науки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галузь науки"
        verbose_name_plural = "Галузі науки"


class Vidannya(models.Model):
    title = models.CharField(max_length=255)
    galuz = models.ForeignKey(GaluzNauki, on_delete=models.CASCADE)
    link = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видання"
        verbose_name_plural = "Видання"