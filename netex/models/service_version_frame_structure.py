from dataclasses import dataclass, field
from typing import Optional

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


@dataclass
class ServiceVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Service_VersionFrameStructure"

    network: Network | None = field(
        default=None,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    additional_networks: NetworksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "additionalNetworks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    directions: DirectionsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_points: RoutePointsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "routePoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_links: RouteLinksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "routeLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    routes: RoutesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_point_properties: FlexiblePointPropertiesRelStructure | None = field(
        default=None,
        metadata={
            "name": "flexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_link_properties: FlexibleLinkPropertiesRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "flexibleLinkProperties",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    common_sections: CommonSectionsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "commonSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    general_sections: GeneralSectionsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "generalSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_links: GroupOfLinksRelStructure | None = field(
        default=None,
        metadata={
            "name": "groupsOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_points: GroupOfPointsRelStructure | None = field(
        default=None,
        metadata={
            "name": "groupsOfPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lines: LinesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_lines: GroupsOfLinesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "groupsOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_displays: DestinationDisplaysInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "destinationDisplays",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    line_networks: LineNetworksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "lineNetworks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    scheduled_stop_points: ScheduledStopPointsInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "scheduledStopPoints",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    service_links: ServiceLinksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "serviceLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_patterns: ServicePatternsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "servicePatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_areas: StopAreasInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "stopAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connections: TransfersInFrameRelStructure | None = field(
        default=None,
        metadata={
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
    stop_assignments: StopAssignmentsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "stopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_points: TimingPointsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "timingPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_links: TimingLinksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "timingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_patterns: TimingPatternsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "timingPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_patterns: JourneyPatternsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_restrictions: TransferRestrictionsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "transferRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    routing_constraint_zones: RoutingConstraintZonesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "routingConstraintZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_exclusions: ServiceExclusionsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "serviceExclusions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_types: TimeDemandTypesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_assignments: TimeDemandTypeAssignmentsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "timeDemandTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timing_link_groups: GroupOfLinksInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "timingLinkGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notices: NoticesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: NoticeAssignmentsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    logical_displays: LogicalDisplaysInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "logicalDisplays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    display_assignments: DisplayAssignmentsInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "displayAssignments",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    passenger_information_equipments: PassengerInformationEquipmentsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "passengerInformationEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
