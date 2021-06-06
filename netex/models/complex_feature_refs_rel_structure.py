from dataclasses import dataclass, field
from typing import Optional
from .complex_feature_ref import ComplexFeatureRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "complexFeatureRefs_RelStructure"

    complex_feature_ref: Optional[ComplexFeatureRef] = field(
        default=None,
        metadata={
            "name": "ComplexFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
