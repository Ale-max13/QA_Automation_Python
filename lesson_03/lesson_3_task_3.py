from address import Address
from mailing import Mailing

from_address = Address("123456", "Москва", "Ленина", "10", "15")
to_address = Address("654321", "Сочи", "Гагарина", "25", "5")

mail = Mailing(to_address, from_address, 500, "TR123456789RU")

print(
    f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment}"
)
