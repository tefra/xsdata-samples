from dataclasses import dataclass, field
from typing import Optional
from netex.models.country_version_structure import CountryVersionStructure
from netex.models.iana_country_tld_enumeration import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Country(CountryVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 2,
            "max_length": 2,
        }
    )
