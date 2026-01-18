from dataclasses import dataclass, field
from decimal import Decimal

from .entity_in_version_structure import DataManagedObjectStructure
from .line_string import LineString
from .link_type_refs_rel_structure import LinkTypeRefsRelStructure
from .multilingual_string import MultilingualString
from .points_on_link_rel_structure import PointsOnLinkRelStructure
from .projections_rel_structure import ProjectionsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Link_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Decimal | None = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types: LinkTypeRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_string: LineString | None = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projections: ProjectionsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passing_through: PointsOnLinkRelStructure | None = field(
        default=None,
        metadata={
            "name": "passingThrough",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
