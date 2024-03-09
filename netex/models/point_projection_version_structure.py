from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .link_ref_structure import LinkRefStructure
from .point_ref_structure import PointRefStructure
from .projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "PointProjection_VersionStructure"

    projected_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedPointRef",
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
    project_to_link_ref: Optional[LinkRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
