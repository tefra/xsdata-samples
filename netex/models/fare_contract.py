from dataclasses import dataclass

from .fare_contract_version_structure import FareContractVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContract(FareContractVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
