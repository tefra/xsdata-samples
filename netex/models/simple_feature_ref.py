from dataclasses import dataclass

from .simple_feature_ref_structure import SimpleFeatureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleFeatureRef(SimpleFeatureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
