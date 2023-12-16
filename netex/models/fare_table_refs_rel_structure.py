from dataclasses import dataclass, field
from typing import List, Union
from .fare_table_ref import FareTableRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTableRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareTableRefs_RelStructure"

    standard_fare_table_ref_or_fare_table_ref: List[Union[StandardFareTableRef, FareTableRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
