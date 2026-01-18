from __future__ import annotations

from dataclasses import dataclass, field

from .compass_bearing16_enumeration import CompassBearing16Enumeration
from .destination_display_views_rel_structure import (
    DestinationDisplayViewsRelStructure,
)
from .flexible_quay_version_structure import FlexibleQuayVersionStructure
from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HailAndRideAreaVersionStructure(FlexibleQuayVersionStructure):
    class Meta:
        name = "HailAndRideArea_VersionStructure"

    bearing_compass: CompassBearing16Enumeration | None = field(
        default=None,
        metadata={
            "name": "BearingCompass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing_degrees: int | None = field(
        default=None,
        metadata={
            "name": "BearingDegrees",
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
    start_point_ref: PointRefStructure | None = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    end_point_ref: PointRefStructure | None = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
