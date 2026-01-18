from dataclasses import dataclass, field

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .operator_view import OperatorView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultConnectionEndStructure:
    transport_mode: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_view: OperatorView | None = field(
        default=None,
        metadata={
            "name": "OperatorView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
