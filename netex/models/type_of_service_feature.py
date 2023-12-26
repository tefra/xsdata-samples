from dataclasses import dataclass
from .type_of_service_feature_value_structure import (
    TypeOfServiceFeatureValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfServiceFeature(TypeOfServiceFeatureValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
