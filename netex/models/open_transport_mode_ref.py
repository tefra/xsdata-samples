from dataclasses import dataclass

from .open_transport_mode_ref_structure import OpenTransportModeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OpenTransportModeRef(OpenTransportModeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
