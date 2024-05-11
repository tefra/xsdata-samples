from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .boarding_positions_rel_structure import BoardingPositionsRelStructure
from .compass_bearing8_enumeration import CompassBearing8Enumeration
from .destination_display_views_rel_structure import (
    DestinationDisplayViewsRelStructure,
)
from .quay_ref_structure import QuayRefStructure
from .quay_type_enumeration import QuayTypeEnumeration
from .stop_place_space_version_structure import StopPlaceSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class QuayVersionStructure(StopPlaceSpaceVersionStructure):
    class Meta:
        name = "Quay_VersionStructure"

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    plate_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destinations: Optional[DestinationDisplayViewsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compass_bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "CompassBearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compass_octant: Optional[CompassBearing8Enumeration] = field(
        default=None,
        metadata={
            "name": "CompassOctant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_type: Optional[QuayTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "QuayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    platform_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PlatformHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    edge_to_track_center_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EdgeToTrackCenterDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_quay_ref: Optional[QuayRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentQuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_positions: Optional[BoardingPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "boardingPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
