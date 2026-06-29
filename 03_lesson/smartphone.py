gitclass Smartphone:
    def __init__(self, brand: str, model: str, phone_number: str):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79111234567"),
    Smartphone("Samsung", "Galaxy S24", "+79222345678"),
    Smartphone("Xiaomi", "14 Pro", "+79333456789"),
    Smartphone("Google", "Pixel 8", "+79444567890"),
    Smartphone("Huawei", "Pura 70", "+79555678901")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    