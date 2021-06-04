from dataclasses import dataclass
from netex.models.open_transport_mode_value_structure import OpenTransportModeValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Submode(OpenTransportModeValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
