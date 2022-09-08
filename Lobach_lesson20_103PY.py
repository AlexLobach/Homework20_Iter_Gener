class CardDeck:  # Объявление функции.
    suits_list = ['Пик', 'Бубей', 'Червей', 'Крестей']  # Список мастей.
    num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Валет", "Дама", "Король", "Туз"]  # Список номиналов.
    count = 0  # Счетчик.

    def __init__(self):  # Инициализатор. В дин. св-ве хранится список всех карт.
        self.card_list = [f'{str(j)} {str(i)}' for i in self.suits_list for j in self.num_list]  # Дин. св-во.

    def __iter__(self):  # Магический метод , для того чтобы объект можно было перебрать итерацией.
        return self  # Возвращает сам итератор.

    def __next__(self):  # Магический метод, при его вызове будет возвращатся следующее значение итератора
        if self.count < 52:  # Если счетчик меншье 52, то
            card_ = self.card_list[
                self.count]  # В перменную записывается соотв. значение из списка по индексу (счетчик)
            self.count += 1  # Счетчик увеличивается на 1
            return card_  # Возвращает значение
        else:
            raise StopIteration  # Вызов исключения


for i in CardDeck():
    print(i)
