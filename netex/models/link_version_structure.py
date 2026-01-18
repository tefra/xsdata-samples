from __future__ import annotations

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

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: None | Decimal = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types: None | LinkTypeRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_string: None | LineString = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projections: None | ProjectionsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passing_through: None | PointsOnLinkRelStructure = field(
        default=None,
        metadata={
            "name": "passingThrough",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
