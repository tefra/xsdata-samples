from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTableRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "StandardFareTableRefs_RelStructure"

    standard_fare_table_ref: Sequence[StandardFareTableRef] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
