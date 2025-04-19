#Класс Store имеет атрибуты: name (название магазина), address (адрес магазина)
# и items (ассортимент товаров в виде словаря).
class Store:
    def __init__(self, name, address):
        # Инициализация атрибутов
        self.name = name # название магазина
        self.address = address
        self.items = {} #это словарь для хранения двух ключей(хар.) названиеи цена

    # Метод для добавления товара в ассортимент
    def add_item(self, item_name, item_price):
        self.items[item_name] = item_price # ключ
        print(f"Товар {item_name} добавлен с ценой {self.name}.") # было item_price

    # Метод для удаления товара из ассортимента, если он есть
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удален.")
        else:
            print(f"Товар {item_name} не найден.")

    # Метод для получения цены товара по его названию
    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    # Метод для обновления цены товара, если товар найден в ассортименте
    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} обновлена на {new_price}.")
        else:
            print(f"Товар {item_name} не найден.")

# Пример использования
store1 = Store("Магазин №1", "Улица 11 Авеню, Москва")
store2 = Store("Магнитус", "Улица Адмирала Серебрякова, Новороссийск")
store3 = Store("Пикси", " Красная площадь, Москва")

# Добавление товаров
store1.add_item("apples", 90)
store2.add_item("bananas", 120)

# Получение цены товара
print(f"Цена яблок: {store1.get_item_price('apples')}")

# Обновление цены товара
store1.update_item_price("apples", 100)

# Удаление товара
store2.remove_item("bananas")

# Попытка получения цены удаленного товара
print(f"Цена бананов: {store2.get_item_price('bananas')}")