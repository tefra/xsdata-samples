from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.type_of_fare_contract_entry import TypeOfFareContractEntry
from netex.models.type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfFareContractEntryRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfFareContractEntry_RelStructure"

    type_of_fare_contract_entry_ref: List[TypeOfFareContractEntryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_contract_entry: List[TypeOfFareContractEntry] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
