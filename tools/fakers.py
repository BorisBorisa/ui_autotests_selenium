from faker import Faker
from datetime import datetime


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        :return: Случайная фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        """
        return self.faker.first_name()

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(start, end)

    def age(self) -> int:
        """
        Генерирует случайный возраст.

        :return: Случайное целое число в диапазоне от 18 до 99.
        """
        return self.integer(18, 99)

    def salary(self) -> int:
        """
        Генерирует случайную зарплату.

        :return: Случайное целое число в диапазоне от 10000 до 50000.
        """
        return self.integer(10000, 50000)

    def word(self) -> str:
        """
        Генерирует случайное слово.

        :return: Случайное слово.
        """
        return self.faker.word()

    def data_time(self) -> datetime:
        """
        Генерирует случайную дату и время.

        :return: Случайная дата и время.
        """
        return self.faker.date_time()


fake = Fake(faker=Faker())
