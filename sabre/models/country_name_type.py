from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class CountryNameType:
    """
    The name or code of a country (e.g. as used in an address or to specify
    citizenship of a traveller).

    Attributes:
        value:
        code: ISO 3166 code for a country.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 64,
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{2}",
        },
    )
