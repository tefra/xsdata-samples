from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_fare_contract_entry_ref import TypeOfFareContractEntryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFareContractEntryRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfFareContractEntryRefs_RelStructure"

    type_of_fare_contract_entry_ref: List[TypeOfFareContractEntryRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractEntryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
