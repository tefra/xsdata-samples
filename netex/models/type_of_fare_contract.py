from dataclasses import dataclass
from .type_of_fare_contract_version_structure import (
    TypeOfFareContractVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareContract(TypeOfFareContractVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
