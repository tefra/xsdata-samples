from dataclasses import dataclass
from .country_version_structure import CountryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Country(CountryVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
