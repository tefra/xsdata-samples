from __future__ import annotations

from dataclasses import dataclass, field

from .common_sections_in_frame_rel_structure import (
    CommonSectionsInFrameRelStructure,
)
from .common_version_frame_structure import CommonVersionFrameStructure
from .destination_displays_in_frame_rel_structure import (
    DestinationDisplaysInFrameRelStructure,
)
from .directions_in_frame_rel_structure import DirectionsInFrameRelStructure
from .display_assignments_in_frame_rel_structure import (
    DisplayAssignmentsInFrameRelStructure,
)
from .flexible_link_properties_rel_structure import (
    FlexibleLinkPropertiesRelStructure,
)
from .flexible_point_properties_rel_structure import (
    FlexiblePointPropertiesRelStructure,
)
from .general_sections_in_frame_rel_structure import (
    GeneralSectionsInFrameRelStructure,
)
from .group_of_links_in_frame_rel_structure import (
    GroupOfLinksInFrameRelStructure,
)
from .group_of_links_rel_structure import GroupOfLinksRelStructure
from .group_of_points_rel_structure import GroupOfPointsRelStructure
from .groups_of_lines_in_frame_rel_structure import (
    GroupsOfLinesInFrameRelStructure,
)
from .journey_patterns_in_frame_rel_structure import (
    JourneyPatternsInFrameRelStructure,
)
from .line_networks_in_frame_rel_structure import (
    LineNetworksInFrameRelStructure,
)
from .lines_in_frame_rel_structure import LinesInFrameRelStructure
from .logical_displays_in_frame_rel_structure import (
    LogicalDisplaysInFrameRelStructure,
)
from .network import Network
from .networks_in_frame_rel_structure import NetworksInFrameRelStructure
from .notice_assignments_in_frame_rel_structure import (
    NoticeAssignmentsInFrameRelStructure,
)
from .notices_in_frame_rel_structure import NoticesInFrameRelStructure
from .passenger_information_equipments_in_frame_rel_structure import (
    PassengerInformationEquipmentsInFrameRelStructure,
)
from .route_links_in_frame_rel_structure import RouteLinksInFrameRelStructure
from .route_points_in_frame_rel_structure import RoutePointsInFrameRelStructure
from .routes_in_frame_rel_structure import RoutesInFrameRelStructure
from .routing_constraint_zones_in_frame_rel_structure import (
    RoutingConstraintZonesInFrameRelStructure,
)
from .scheduled_stop_points_in_frame_rel_structure import (
    ScheduledStopPointsInFrameRelStructure,
)
from .service_exclusions_in_frame_rel_structure import (
    ServiceExclusionsInFrameRelStructure,
)
from .service_links_in_frame_rel_structure import (
    ServiceLinksInFrameRelStructure,
)
from .service_patterns_in_frame_rel_structure import (
    ServicePatternsInFrameRelStructure,
)
from .stop_areas_in_frame_rel_structure import StopAreasInFrameRelStructure
from .stop_assignments_in_frame_rel_structure import (
    StopAssignmentsInFrameRelStructure,
)
from .tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from .time_demand_type_assignments_in_frame_rel_structure import (
    TimeDemandTypeAssignmentsInFrameRelStructure,
)
from .time_demand_types_in_frame_rel_structure import (
    TimeDemandTypesInFrameRelStructure,
)
from .timing_links_in_frame_rel_structure import TimingLinksInFrameRelStructure
from .timing_patterns_in_frame_rel_structure import (
    TimingPatternsInFrameRelStructure,
)
from .timing_points_in_frame_rel_structure import (
    TimingPointsInFrameRelStructure,
)
from .transfer_restrictions_in_frame_rel_structure import (
    TransferRestrictionsInFrameRelStructure,
)
from .transfers_in_frame_rel_structure import TransfersInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Service_VersionFrameStructure"

    network: None | Network = field(
        default=None,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    additional_networks: None | NetworksInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "additionalNetworks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    directions: None | DirectionsInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_points: None | RoutePointsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "routePoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_links: None | RouteLinksInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "routeLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    routes: None | RoutesInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_point_properties: None | FlexiblePointPropertiesRelStructure = (
        field(
            default=None,
            metadata={
                "name": "flexiblePointProperties",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    flexible_link_properties: None | FlexibleLinkPropertiesRelStructure = (
        field(
            default=None,
            metadata={
                "name": "flexibleLinkProperties",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    common_sections: None | CommonSectionsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "commonSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    general_sections: None | GeneralSectionsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "generalSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_links: None | GroupOfLinksRelStructure = field(
        default=None,
        metadata={
            "name": "groupsOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_points: None | GroupOfPointsRelStructure = field(
        default=None,
        metadata={
            "name": "groupsOfPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lines: None | LinesInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_lines: None | GroupsOfLinesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "groupsOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_displays: None | DestinationDisplaysInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "destinationDisplays",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    line_networks: None | LineNetworksInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "lineNetworks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    scheduled_stop_points: None | ScheduledStopPointsInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "scheduledStopPoints",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    service_links: None | ServiceLinksInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "serviceLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_patterns: None | ServicePatternsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "servicePatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_areas: None | StopAreasInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "stopAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connections: None | TransfersInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_zones: None | TariffZonesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_assignments: None | StopAssignmentsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "stopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_points: None | TimingPointsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "timingPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_links: None | TimingLinksInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "timingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_patterns: None | TimingPatternsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "timingPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_patterns: None | JourneyPatternsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_restrictions: None | TransferRestrictionsInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "transferRestrictions",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    routing_constraint_zones: (
        None | RoutingConstraintZonesInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "routingConstraintZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_exclusions: None | ServiceExclusionsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "serviceExclusions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_types: None | TimeDemandTypesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_assignments: (
        None | TimeDemandTypeAssignmentsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "timeDemandTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_link_groups: None | GroupOfLinksInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "timingLinkGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notices: None | NoticesInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: None | NoticeAssignmentsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    logical_displays: None | LogicalDisplaysInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "logicalDisplays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    display_assignments: None | DisplayAssignmentsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "displayAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_information_equipments: (
        None | PassengerInformationEquipmentsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "passengerInformationEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
