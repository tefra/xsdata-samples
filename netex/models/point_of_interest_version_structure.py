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

    classifications: PointOfInterestClassificationsViewsRelStructure | None = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    spaces: PointOfInterestSpacesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    near_topographic_places: TopographicPlaceRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "nearTopographicPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_links: SitePathLinksRelStructure | None = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_junctions: PathJunctionsRelStructure | None = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: AccessesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: NavigationPathsRelStructure | None = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
