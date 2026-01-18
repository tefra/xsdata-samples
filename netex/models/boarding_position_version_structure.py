from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .boarding_position_type_enumeration import BoardingPositionTypeEnumeration
from .entrance_refs_rel_structure import EntranceRefsRelStructure
from .stop_place_space_version_structure import StopPlaceSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPositionVersionStructure(StopPlaceSpaceVersionStructure):
    class Meta:
        name = "BoardingPosition_VersionStructure"

    public_code: None | str = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_position_type: None | BoardingPositionTypeEnumeration = field(
        default=None,
        metadata={
            "name": "BoardingPositionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_position_entrances: None | EntranceRefsRelStructure = field(
        default=None,
        metadata={
            "name": "boardingPositionEntrances",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    platform_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "PlatformHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    edge_to_track_center_distance: None | Decimal = field(
        default=None,
        metadata={
            "name": "EdgeToTrackCenterDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
