# Generated by Django 5.1.4 on 2024-12-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0003_alter_article_author_alter_article_doi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, default='Автор отсутствует', max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='doi',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='link',
            field=models.URLField(blank=True, default='Ссылка отсутствует', max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=1500),
        ),
    ]
