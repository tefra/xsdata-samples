from __future__ import annotations

from dataclasses import dataclass, field

from .compass_bearing16_enumeration import CompassBearing16Enumeration
from .destination_display_views_rel_structure import (
    DestinationDisplayViewsRelStructure,
)
from .flexible_quay_version_structure import FlexibleQuayVersionStructure
from .point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HailAndRideAreaVersionStructure(FlexibleQuayVersionStructure):
    class Meta:
        name = "HailAndRideArea_VersionStructure"

    bearing_compass: None | CompassBearing16Enumeration = field(
        default=None,
        metadata={
            "name": "BearingCompass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing_degrees: None | int = field(
        default=None,
        metadata={
            "name": "BearingDegrees",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destinations: None | DestinationDisplayViewsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_point_ref: PointRefStructure = field(
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_point_ref: PointRefStructure = field(
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
