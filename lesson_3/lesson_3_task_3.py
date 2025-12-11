from address import Address #Импортируем класс Address
from mailing import Mailing #Импортируем класс Mailing

to_address = Address("601916", "Ковров", "Кирова", "104", "7")
from_address = Address("153001", "Иваново", "Куконковых", "17", "25")

#Создаём экземпляр класса Mailing
mailing = Mailing(to_address, from_address, 800, "TRACK234")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
