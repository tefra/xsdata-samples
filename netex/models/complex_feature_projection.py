from dataclasses import dataclass
from netex.models.complex_feature_projection_version_structure import ComplexFeatureProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureProjection(ComplexFeatureProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
