from dataclasses import dataclass, field
from typing import Optional
from netex.models.accesses_rel_structure import AccessesRelStructure
from netex.models.navigation_paths_rel_structure import NavigationPathsRelStructure
from netex.models.path_junctions_rel_structure import PathJunctionsRelStructure
from netex.models.point_of_interest_classifications_views_rel_structure import PointOfInterestClassificationsViewsRelStructure
from netex.models.point_of_interest_spaces_rel_structure import PointOfInterestSpacesRelStructure
from netex.models.site_path_links_rel_structure import SitePathLinksRelStructure
from netex.models.site_version_structure import SiteVersionStructure
from netex.models.topographic_place_refs_rel_structure import TopographicPlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestVersionStructure(SiteVersionStructure):
    class Meta:
        name = "PointOfInterest_VersionStructure"

    classifications: Optional[PointOfInterestClassificationsViewsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    spaces: Optional[PointOfInterestSpacesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    near_topographic_places: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "nearTopographicPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_links: Optional[SitePathLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junctions: Optional[PathJunctionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accesses: Optional[AccessesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_paths: Optional[NavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
