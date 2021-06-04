from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.fare_contract import FareContract
from netex.models.fare_contract_ref import FareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareContracts_RelStructure"

    fare_contract_ref: List[FareContractRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract: List[FareContract] = field(
        default_factory=list,
        metadata={
            "name": "FareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
