from dataclasses import dataclass
from netex.models.layer_version_structure import LayerVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Layer(LayerVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
