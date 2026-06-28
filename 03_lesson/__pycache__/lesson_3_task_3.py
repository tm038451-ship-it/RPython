from address import Address
from mailing import Mailing

to_addr = Address("44386", "Шилан", "Школьная", "12", "2")

from_addr = Address("443051", "Самара", "Проспект Металлургов", "82", "7")

mailing_item = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="RU123456789"
)

print(
    f"Отправление {mailing_item.track} из "
    f"{mailing_item.from_address.index}, {mailing_item.from_address.city}, "
    f"{mailing_item.from_address.street}, {mailing_item.from_address.house} - {mailing_item.from_address.apartment} в "
    f"{mailing_item.to_address.index}, {mailing_item.to_address.city}, "
    f"{mailing_item.to_address.street}, {mailing_item.to_address.house} - {mailing_item.to_address.apartment}. "
    f"Стоимость {mailing_item.cost} рублей."
    
)