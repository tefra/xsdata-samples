from __future__ import annotations

from dataclasses import dataclass, field

from .accesses_in_frame_rel_structure import AccessesInFrameRelStructure
from .addresses_in_frame_rel_structure import AddressesInFrameRelStructure
from .check_constraint_delays_in_frame_rel_structure import (
    CheckConstraintDelaysInFrameRelStructure,
)
from .check_constraint_in_frame_rel_structure import (
    CheckConstraintInFrameRelStructure,
)
from .check_constraint_throughputs_in_frame_rel_structure import (
    CheckConstraintThroughputsInFrameRelStructure,
)
from .common_version_frame_structure import CommonVersionFrameStructure
from .countries_in_frame_rel_structure import CountriesInFrameRelStructure
from .flexible_stop_places_in_frame_rel_structure import (
    FlexibleStopPlacesInFrameRelStructure,
)
from .groups_of_stop_places_in_frame_rel_structure import (
    GroupsOfStopPlacesInFrameRelStructure,
)
from .groups_of_tariff_zones_in_frame_rel_structure import (
    GroupsOfTariffZonesInFrameRelStructure,
)
from .navigation_paths_in_frame_rel_structure import (
    NavigationPathsInFrameRelStructure,
)
from .parkings_in_frame_rel_structure import ParkingsInFrameRelStructure
from .path_junctions_in_frame_rel_structure import (
    PathJunctionsInFrameRelStructure,
)
from .path_links_in_frame_rel_structure import PathLinksInFrameRelStructure
from .point_of_interest_classification_hierarchies_in_frame_rel_structure import (
    PointOfInterestClassificationHierarchiesInFrameRelStructure,
)
from .point_of_interest_classifications_in_frame_rel_structure import (
    PointOfInterestClassificationsInFrameRelStructure,
)
from .points_of_interest_in_frame_rel_structure import (
    PointsOfInterestInFrameRelStructure,
)
from .site_facility_sets_in_frame_rel_structure import (
    SiteFacilitySetsInFrameRelStructure,
)
from .stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from .tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from .taxi_ranks_in_frame_rel_structure import TaxiRanksInFrameRelStructure
from .topographic_places_in_frame_rel_structure import (
    TopographicPlacesInFrameRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Site_VersionFrameStructure"

    countries: CountriesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topographic_places: TopographicPlacesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "topographicPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    addresses: AddressesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: AccessesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_stop_places: GroupsOfStopPlacesInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "groupsOfStopPlaces",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    stop_places: StopPlacesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "stopPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_stop_places: FlexibleStopPlacesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "flexibleStopPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    taxi_ranks: TaxiRanksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "taxiRanks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_of_interest: PointsOfInterestInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "pointsOfInterest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parkings: ParkingsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: NavigationPathsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_links: PathLinksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_junctions: PathJunctionsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraints: CheckConstraintInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "checkConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraint_delays: (
        CheckConstraintDelaysInFrameRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "checkConstraintDelays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraint_throughputs: (
        CheckConstraintThroughputsInFrameRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "checkConstraintThroughputs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_of_interest_classifications: (
        PointOfInterestClassificationsInFrameRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "pointOfInterestClassifications",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_of_interest_classification_hierarchies: (
        PointOfInterestClassificationHierarchiesInFrameRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "pointOfInterestClassificationHierarchies",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_zones: TariffZonesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_tariff_zones: GroupsOfTariffZonesInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "groupsOfTariffZones",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    site_facility_sets: SiteFacilitySetsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "siteFacilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
