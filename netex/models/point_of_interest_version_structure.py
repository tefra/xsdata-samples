from __future__ import annotations

from dataclasses import dataclass, field

from .accesses_rel_structure import AccessesRelStructure
from .navigation_paths_rel_structure import NavigationPathsRelStructure
from .path_junctions_rel_structure import PathJunctionsRelStructure
from .point_of_interest_classifications_views_rel_structure import (
    PointOfInterestClassificationsViewsRelStructure,
)
from .point_of_interest_spaces_rel_structure import (
    PointOfInterestSpacesRelStructure,
)
from .site_path_links_rel_structure import SitePathLinksRelStructure
from .site_version_structure import SiteVersionStructure
from .topographic_place_refs_rel_structure import (
    TopographicPlaceRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestVersionStructure(SiteVersionStructure):
    class Meta:
        name = "PointOfInterest_VersionStructure"

    classifications: None | PointOfInterestClassificationsViewsRelStructure = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    spaces: None | PointOfInterestSpacesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    near_topographic_places: None | TopographicPlaceRefsRelStructure = field(
        default=None,
        metadata={
            "name": "nearTopographicPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_links: None | SitePathLinksRelStructure = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_junctions: None | PathJunctionsRelStructure = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: None | AccessesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: None | NavigationPathsRelStructure = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
