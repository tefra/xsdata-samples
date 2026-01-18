from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .stop_area_ref_structure import StopAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAreaRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "stopAreaRefs_RelStructure"

    stop_area_ref: Iterable[StopAreaRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
