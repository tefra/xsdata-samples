from dataclasses import dataclass
from .transport_type_version_structure import TransportTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportType1(TransportTypeVersionStructure):
    class Meta:
        name = "TransportType"
        namespace = "http://www.netex.org.uk/netex"
