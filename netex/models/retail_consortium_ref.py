from dataclasses import dataclass
from netex.models.retail_consortium_ref_structure import RetailConsortiumRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailConsortiumRef(RetailConsortiumRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
