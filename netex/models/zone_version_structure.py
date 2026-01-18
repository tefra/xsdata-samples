from dataclasses import dataclass, field

from .group_of_points_version_structure import GroupOfPointsVersionStructure
from .multi_surface import MultiSurface
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

    types: TypeOfZoneRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    centroid: SimplePointVersionStructure | None = field(
        default=None,
        metadata={
            "name": "Centroid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    polygon_or_multi_surface: Polygon | MultiSurface | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "MultiSurface",
                    "type": MultiSurface,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        },
    )
    projections: ProjectionsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_zone_ref: ZoneRefStructure | None = field(
        default=None,
        metadata={
            "name": "ParentZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
