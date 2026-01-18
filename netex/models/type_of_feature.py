from __future__ import annotations

from dataclasses import dataclass

from .type_of_feature_value_structure import TypeOfFeatureValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFeature(TypeOfFeatureValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
