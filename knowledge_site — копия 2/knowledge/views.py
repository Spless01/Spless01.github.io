from django.shortcuts import render
from knowledge.models import Article, KnowledgeField
from django.http import JsonResponse
from knowledge.models import Vidannya, GaluzNauki


def home(request):
    return render(request, 'knowledge/home.html')

def search_articles(request):
    field_id = request.GET.get("field", "")
    query = request.GET.get("query", "")

    print(f"ID из формы: {field_id}")
    # Получаем список всех галузей знань
    fields = KnowledgeField.objects.all()

    # Начальный запрос ко всем статьям
    articles = Article.objects.all()

    # Фильтрация по выбранной галузі знань
    if field_id:
        articles = articles.filter(field_id=field_id)

    # Фильтрация по названию статьи
    if query:
        articles = articles.filter(title__icontains=query)

    # Отправка данных в шаблон
    return render(request, "knowledge/search.html", {
        "fields": fields,
        "articles": articles,
        "selected_field": field_id,
        "query": query
    })


def search_vidannya(request):
    field = request.GET.get("field", None)
    if field:
        vidannya_list = Vidannya.objects.filter(galuz__name=field)
    else:
        vidannya_list = Vidannya.objects.all()

    galuz = GaluzNauki.objects.all()
    context = {
        'vidannya_list': vidannya_list,
        'galuz': galuz,
    }
    return render(request, 'knowledge/vidannya.html', context)
