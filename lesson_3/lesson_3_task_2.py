from smartphone import Smartphone #Импортируем класс Smartphone
#Объявляем переменную  catalog и создаём список
catalog = []

#Наполняем спмсок пятью разными экземплярамии класса Smartphone
catalog.append(Smartphone("Apple", "IPhone 14", "+79001234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79007654321"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79012345678"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79019876543"))
catalog.append(Smartphone("Google", "Pixel 6", "+79023456789"))

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.number}")
