from dataclasses import dataclass
from netex.models.fare_contract_ref_structure import FareContractRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractRef(FareContractRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
