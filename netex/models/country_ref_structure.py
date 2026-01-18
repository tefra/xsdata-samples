from dataclasses import dataclass, field
from typing import Optional

from .iana_country_tld_enumeration import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CountryRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    ref: IanaCountryTldEnumeration | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref_principality: str | None = field(
        default=None,
        metadata={
            "name": "refPrincipality",
            "type": "Attribute",
        },
    )
