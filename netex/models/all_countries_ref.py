from dataclasses import dataclass
from netex.models.all_countries_ref_structure import AllCountriesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllCountriesRef(AllCountriesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
