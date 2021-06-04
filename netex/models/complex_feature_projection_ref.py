from dataclasses import dataclass
from netex.models.complex_feature_projection_ref_structure import ComplexFeatureProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureProjectionRef(ComplexFeatureProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
