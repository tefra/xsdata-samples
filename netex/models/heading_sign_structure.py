from dataclasses import dataclass, field
from typing import Optional, Union

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .destination_display_ref import DestinationDisplayRef
from .direction_ref import DirectionRef
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .multilingual_string import MultilingualString
from .sign_equipment_version_structure import SignEquipmentVersionStructure
from .transport_submode import TransportSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HeadingSignStructure(SignEquipmentVersionStructure):
    place_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    line_ref: Optional[Union[FlexibleLineRef, LineRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    line_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "LineName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_map: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineMap",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DirectionName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinePublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
