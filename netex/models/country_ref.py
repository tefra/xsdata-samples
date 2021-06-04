from dataclasses import dataclass
from netex.models.country_ref_structure import CountryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CountryRef(CountryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
