from dataclasses import dataclass
from netex.models.unknown_extensions_error_structure import UnknownExtensionsErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownExtensionsError(UnknownExtensionsErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
