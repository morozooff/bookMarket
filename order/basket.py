
from django.conf import settings
from market.models import Book


class Basket(object):

    def __init__(self, request):
        # получаем с запроса данные о текущей сесии
        self.session = request.session
        # по тегу из настроек пытаемся получить из сессии корзину
        basket = self.session.get(settings.BASKET_SESSION_ID)

        # если корзину не получилось получить, то создаем ее с тэгом 'basket'
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        # полученную или созданную корзину возвращаем самому объекту
        self.basket = basket

    # функция для добавления в корзину или обновления колличества
    def add(self, book, quantity = 1, update_quantity = False ):
        # при передаче объекта книги в корзину, берем id этой книги
        book_id = str(book.id)
        # если такая id еще не содержится в словаре корзине
        if book_id not in self.basket:
            # то мы создаем новый элемент словаря с ключом 'book_id' и с нулевым параметром колличества и со стоимостью книги
            self.basket[book_id] = {'quantity' : 0, 'cost': str(book.cost)}

        # если нужно обновить колличество
        if update_quantity:
            # то в поле колличество записываем новое значение
            self.basket[book_id]['quantity'] = quantity
        else:
            # иначе обновляем значение колличество на плюс один
            self.basket[book_id]['quantity'] += quantity
        # сохраняем состояние объекта
        self.save()

    def save(self):
        # Обновление сесси basket
        self.session[settings.BASKET_SESSION_ID] = self.basket

        # Отметить сеанс как измененный, чтобы убедиться, что он сохранен


    def remove(self, book):
        book_id = str(book.id)

        if book_id in self.basket:
            self.basket[book_id]['quantity'] -= 1
            self.save()


    # перебор элементов в корзине и получение из БД
    def __iter__(self):
        # получаем все ключи словаря, которые являются id книг
        book_ids = self.basket.keys()
        # получаем из Бд все экземпляры с id из корзины
        books = Book.objects.filter(id__in = book_ids)

        # для каждого экземпляра книги из полученных из бд
        for book in books:

            # записываем в словарь корзины с ключом book.id в значение 'book' сам экземпляр
            self.basket[str(book.id)]['book'] = book

        # для каждого значения из корзины записываем
        for item in self.basket.values():
            # значение общей стоимости равно произведению стоимости книги на колличество экземпляров этой книги
            item['total_cost'] = int(item['cost']) * int(item['quantity'])
            # все это происходит каждый раз при итерации
            yield item


    # определяем len для корзины
    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())


        # для общей стоимости корзины
    def get_total_price(self):
        total_price = 0
        for item in self.basket.values():
            total_price += item['total_cost']
        return total_price


        # для очистки сеанса корзины
    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True





