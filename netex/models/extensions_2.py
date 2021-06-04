from dataclasses import dataclass
from netex.models.extensions_structure_2 import ExtensionsStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Extensions2(ExtensionsStructure2):
    class Meta:
        name = "Extensions"
        namespace = "http://www.netex.org.uk/netex"
