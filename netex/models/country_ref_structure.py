from __future__ import annotations

from dataclasses import dataclass, field

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
    ref: None | IanaCountryTldEnumeration = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref_principality: None | str = field(
        default=None,
        metadata={
            "name": "refPrincipality",
            "type": "Attribute",
        },
    )
