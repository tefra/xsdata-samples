from dataclasses import dataclass, field
from typing import Optional
from .iana_country_tld_enumeration import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CountryRefStructure:
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 2,
            "max_length": 2,
        }
    )
    ref_principality: Optional[str] = field(
        default=None,
        metadata={
            "name": "refPrincipality",
            "type": "Attribute",
        }
    )
