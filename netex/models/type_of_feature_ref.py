from dataclasses import dataclass

from .type_of_feature_ref_structure import TypeOfFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFeatureRef(TypeOfFeatureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
