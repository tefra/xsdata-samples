from dataclasses import dataclass, field
from typing import Optional

from .group_of_points_version_structure import GroupOfPointsVersionStructure
from .polygon import Polygon
from .projections_rel_structure import ProjectionsRelStructure
from .simple_point_version_structure import SimplePointVersionStructure
from .type_of_zone_refs_rel_structure import TypeOfZoneRefsRelStructure
from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZoneVersionStructure(GroupOfPointsVersionStructure):
    class Meta:
        name = "Zone_VersionStructure"

    types: Optional[TypeOfZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    centroid: Optional[SimplePointVersionStructure] = field(
        default=None,
        metadata={
            "name": "Centroid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projections: Optional[ProjectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
