from dataclasses import dataclass, field
from typing import Optional

from .point_ref_structure import PointRefStructure
from .point_refs_rel_structure import PointRefsRelStructure
from .projection_version_structure import ProjectionVersionStructure
from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZoneProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "ZoneProjection_VersionStructure"

    projected_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    project_to_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    project_to_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points: Optional[PointRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
