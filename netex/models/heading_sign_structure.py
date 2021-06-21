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
    choice: List[object] = field(
        default_factory=list,
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
                {
                    "name": "LineName",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportMode",
                    "type": VehicleModeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportSubmode",
                    "type": TransportSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineMap",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionRef",
                    "type": DirectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DirectionName",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DestinationDisplayRef",
                    "type": DestinationDisplayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinePublicCode",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
