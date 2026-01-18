from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .series_constraint_ref import SeriesConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraintRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "seriesConstraintRefs_RelStructure"

    series_constraint_ref: Iterable[SeriesConstraintRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
