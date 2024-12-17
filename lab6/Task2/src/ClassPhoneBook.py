class PhoneBook:
    """
    Класс для реализации работы телефонной книги
    """
    def __init__(self) -> None:
        self.phone_book = dict()

    def add_person(self, name: str, number: int) -> None:
        """
        функция для добавления человека
        :param name: str
        :param number: int
        :return: None
        """
        self.phone_book[number] = name

    def del_number(self, number: int) -> None:
        """
        функция для удаления человека по номеру
        :param number: int
        :return: None
        """
        if number in self.phone_book.keys():
            del self.phone_book[number]

    def find_number(self, number: int) -> str:
        """
        функция для нахождения человека по номеру
        :param number: int
        :return: str
        """
        if number in self.phone_book.keys():
            return self.phone_book[number]
        return "not found"
