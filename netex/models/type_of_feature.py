from dataclasses import dataclass
from netex.models.type_of_feature_value_structure import TypeOfFeatureValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfFeature(TypeOfFeatureValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
