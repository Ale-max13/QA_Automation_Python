from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79001112233"),
    Smartphone("Samsung", "Galaxy S23", "+79002223344"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79003334455"),
    Smartphone("Google", "Pixel 7", "+79004445566"),
    Smartphone("Huawei", "P50 Pro", "+79005556677"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
