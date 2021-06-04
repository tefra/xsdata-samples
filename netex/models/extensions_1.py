from dataclasses import dataclass
from netex.models.extensions_structure_1 import ExtensionsStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Extensions1(ExtensionsStructure1):
    class Meta:
        name = "Extensions"
        namespace = "http://www.siri.org.uk/siri"
