from dataclasses import dataclass
from netex.models.complex_feature_ref_structure import ComplexFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ComplexFeatureRef(ComplexFeatureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
