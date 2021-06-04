from dataclasses import dataclass, field
from typing import List
from netex.models.fare_table_ref import FareTableRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTableRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareTableRefs_RelStructure"

    standard_fare_table_ref: List[StandardFareTableRef] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_table_ref: List[FareTableRef] = field(
        default_factory=list,
        metadata={
            "name": "FareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
