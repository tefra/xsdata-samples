from dataclasses import dataclass, field
from typing import List
from netex.models.layer_ref import LayerRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LayerRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "layerRefs_RelStructure"

    layer_ref: List[LayerRef] = field(
        default_factory=list,
        metadata={
            "name": "LayerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
