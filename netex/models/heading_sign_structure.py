from dataclasses import dataclass, field
from typing import List, Optional
from .destination_display_ref import DestinationDisplayRef
from .direction_ref import DirectionRef
from .flexible_line_ref import FlexibleLineRef
from .line_ref import LineRef
from .multilingual_string import MultilingualString
from .sign_equipment_version_structure import SignEquipmentVersionStructure
from .transport_submode import TransportSubmode
from .vehicle_mode_enumeration import VehicleModeEnumeration

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
        }
    )
    flexible_line_ref: List[FlexibleLineRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "LineName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_map: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineMap",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DirectionName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LinePublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
