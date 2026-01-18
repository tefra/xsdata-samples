from dataclasses import dataclass, field
from decimal import Decimal

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

    public_code: str | None = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    plate_code: str | None = field(
        default=None,
        metadata={
            "name": "PlateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_code: int | None = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destinations: DestinationDisplayViewsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compass_bearing: float | None = field(
        default=None,
        metadata={
            "name": "CompassBearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compass_octant: CompassBearing8Enumeration | None = field(
        default=None,
        metadata={
            "name": "CompassOctant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_type: QuayTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "QuayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    platform_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "PlatformHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    edge_to_track_center_distance: Decimal | None = field(
        default=None,
        metadata={
            "name": "EdgeToTrackCenterDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_quay_ref: QuayRefStructure | None = field(
        default=None,
        metadata={
            "name": "ParentQuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_positions: BoardingPositionsRelStructure | None = field(
        default=None,
        metadata={
            "name": "boardingPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
