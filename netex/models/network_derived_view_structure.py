from __future__ import annotations

from dataclasses import dataclass, field

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .derived_view_structure import DerivedViewStructure
from .multilingual_string import MultilingualString
from .network_ref import NetworkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "Network_DerivedViewStructure"

    network_ref: None | NetworkRef = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: None | AllVehicleModesOfTransportEnumeration = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
