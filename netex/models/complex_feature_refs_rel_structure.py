from __future__ import annotations

from dataclasses import dataclass, field

from .complex_feature_ref import ComplexFeatureRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "complexFeatureRefs_RelStructure"

    complex_feature_ref: ComplexFeatureRef = field(
        metadata={
            "name": "ComplexFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
