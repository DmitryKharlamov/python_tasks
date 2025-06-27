from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    metadata = models.JSONField(default=dict)

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

#Найди всех авторов с именем «John».
 Author.objects.filter(first_name="john")

#Найди всех авторов, кроме тех, у кого фамилия «Doe».
Author.objects.exclude(last_name="Doe")
from django.db.models import Q
Author.objects.filter(~Q(last_name="Doe"))

#Найди все книги, цена которых меньше 500.
Book.objects.filter(price__lt=500)

#Найди все книги с ценой не более 300.
Book.objects.filter(price__lte=300)

#Найди все книги дороже 1000.
Book.objects.filter(price__gt=1000)

#Найди все книги с ценой от 750 и выше.
Book.objects.filter(price__gte=750)

#Найди все книги, содержащие слово «django» в названии.
Book.objects.filter(title__contains=”django”)

#Найди книги, в названии которых есть «python» (без учёта регистра).
Book.objects.filter(title__icontains=”python”)

#Найди книги, название которых начинается со слова «Advanced».
Book.objects.filter(title__startswith=’Advanced’)

#Найди книги, название которых начинается с «pro» (игнорируя регистр).
Book.objects.filter(title__istartswith=”pro”)

#Найди книги, название которых заканчивается на слово «Guide».
Book.objects.filter(title__endswith=”Guide”)

#Найди книги, название которых заканчивается на «tutorial» (без учёта регистра).
Book.objects.filter(title__iendswith=”tutorial”)

#Найди все отзывы без комментариев.
Review.objects.filter(comment__isnull=True)

#Найди все отзывы, у которых есть комментарий.
Review.objects.filter(comment__isnull=False)

#Найди авторов с идентификаторами 1, 3 и 5.
Author.objects.filter(id__in=[1,3,5])

#Найди книги, опубликованные с 1 января по 31 декабря 2023 года.
from datetime import datetime
Book.objects.filter(published_date__gte=datetime(2023,1, 1),
                    published_date__lte=datetime(2023, 12, 31, 23, 59, 59))

#Найди книги, название которых начинается со слова «Python».
Book.objects.filter(title__regex=r’^python’)

#Найди авторов, чья фамилия начинается на «Mc» (игнорируя регистр).
Author.objects.filter(last_name__iregex=r’^Mc’)

#Найди книги, опубликованные в 2024 году.
Book.objects.filter(published_date__year=2024)

#Найди книги, опубликованные в июне.
Book.objects.filter(published_date__month=6)

#Найди отзывы, оставленные 11-го числа любого месяца.
Review.objects.filter(created_at__day=11)

#Найди книги, опубликованные на 23-й неделе года.
Book.objects.filter(published_date__week=23)

#Найди отзывы, оставленные во вторник.
Review.objects.filter(created_at__week_day=3)

#Найди книги, опубликованные во втором квартале года.
Book.objects.filter(published_date__quarter=2)

#Найди отзывы, сделанные в определённую дату.
Review.objects.filter(created_at__date=’YYY-MM-DD’)

#Найди отзывы, сделанные ровно в 15:30.
Review.objects.filter(created_at__hour=15, created_at__minute=30)

#Найди отзывы, сделанные в 15 часов.
Review.objects.filter(created_at__hour=15)

#Найди отзывы, сделанные в 30 минут любого часа.
Review.objects.filter(created_at__minute=30)

#Hайди отзывы, созданные в момент, когда секунды были равны 0.
Review.objects.filter(created_at__second=0)

#Найди книги, написанные автором с почтой «author@example.com».
Book.objects.filter(author__email=’author@example.com’)

#Найди книги авторов, чья фамилия содержит «smith» (без учёта регистра).
Book.objects.filter(author__last_name__icontains=’smith’)

#Найди авторов, написавших более пяти книг.
from django.db.models import Count
Author.objects.annotate(count_book=Count(books)).filter(count_book__gt=5)

#Найди книги, у которых значение ключа «genre» равно «fiction».
Book.objects.filter(metadata__genre=’fictiom’)

#Найди книги, где значение ключа «tags» содержит слово «bestseller» (игнорируя регистр).
Book.objects.filter(metadata__tags__icontains=’bestseller’)

#Найди книги, у которых цена равна скидке.
Book.objects.filter(price=F(‘discount’))

#Найди книги, у которых цена больше скидки.
Book.objects.filter(price__gt=F(‘discount’)

#Найди авторов с именем «Alice» или с фамилией, не равной «Brown»
Author.objects.filter(Q(first_name=’Alice’) | ~Q(last_name=’Brown’))

#Подсчитай количество книг каждого автора.
Author.objects.annotate(count_book=Count(books))

#Подсчитай средний рейтинг каждой книги.
Books.objects.annotate(rating_book=Avg(reviews__rating))

#П#осчитай окончательную цену книги (цена минус скидка).
Books.objects.annotate(final_price=(F(‘price’)-F(‘discount’))

#Получи список книг и авторов так, чтобы выполнить всего один SQL-запрос.
Book.objects.select_related(‘author’)

#Получи список авторов и всех их книг так, чтобы было выполнено ровно два SQL-запроса.
Book.objects.prefetch_related(‘author’)
