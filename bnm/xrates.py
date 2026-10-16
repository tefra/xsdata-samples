import datetime
from dataclasses import asdict, dataclass, field
from decimal import Decimal

import requests
from xsdata.formats.dataclass.parsers import XmlParser

"""https://bnm.md/en/content/official-exchange-rates"""


@dataclass
class Currency:
    id: int = field(metadata={"type": "Attribute", "name": "ID"})
    name: str = field(metadata={"type": "Element", "name": "Name"})
    num_code: int = field(metadata={"type": "Element", "name": "NumCode"})
    iso_code: str = field(metadata={"type": "Element", "name": "CharCode"})
    nominal: int = field(metadata={"type": "Element", "name": "Nominal"})
    value: Decimal = field(metadata={"type": "Element", "name": "Value"})


@dataclass
class Currencies:
    class Meta:
        name = "ValCurs"

    date: str = field(metadata={"type": "Attribute", "name": "Date"})
    name: str = field(metadata={"type": "Attribute"})
    values: list[Currency] = field(
        default_factory=list, metadata={"type": "Element", "name": "Valute"}
    )


def fetch():
    now = datetime.datetime.now()
    today = now.strftime("%d.%m.%Y")
    url = f"https://bnm.md/en/official_exchange_rates?get_xml=1&date={today}"

    response = requests.get(url)
    response.raise_for_status()

    return XmlParser().from_string(response.text, Currencies)


if __name__ == "__main__":
    from pprint import pprint

    pprint(asdict(fetch()))
