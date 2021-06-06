from dataclasses import dataclass, field
from typing import List, Optional
from .group_of_lines_ref import GroupOfLinesRef
from .line_refs_rel_structure import LineRefsRelStructure
from .network_ref import NetworkRef
from .points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from .zone_use_enumeration import ZoneUseEnumeration
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutingConstraintZoneVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "RoutingConstraintZone_VersionStructure"

    zone_use: Optional[ZoneUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_in_pattern: Optional[PointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lines: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network_ref: List[NetworkRef] = field(
        default_factory=list,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    group_of_lines_ref: Optional[GroupOfLinesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
