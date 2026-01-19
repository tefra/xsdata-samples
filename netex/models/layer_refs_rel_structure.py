from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .layer_ref import LayerRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LayerRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "layerRefs_RelStructure"

    layer_ref: Sequence[LayerRef] = field(
        default_factory=list,
        metadata={
            "name": "LayerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
