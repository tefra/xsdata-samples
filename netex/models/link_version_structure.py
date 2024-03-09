from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
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

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    types: Optional[LinkTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
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
    passing_through: Optional[PointsOnLinkRelStructure] = field(
        default=None,
        metadata={
            "name": "passingThrough",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
