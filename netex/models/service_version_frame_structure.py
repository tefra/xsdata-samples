from dataclasses import dataclass, field
from typing import Optional
from netex.models.common_sections_in_frame_rel_structure import CommonSectionsInFrameRelStructure
from netex.models.common_version_frame_structure import CommonVersionFrameStructure
from netex.models.destination_displays_in_frame_rel_structure import DestinationDisplaysInFrameRelStructure
from netex.models.directions_in_frame_rel_structure import DirectionsInFrameRelStructure
from netex.models.display_assignments_in_frame_rel_structure import DisplayAssignmentsInFrameRelStructure
from netex.models.flexible_link_properties_rel_structure import FlexibleLinkPropertiesRelStructure
from netex.models.flexible_point_properties_rel_structure import FlexiblePointPropertiesRelStructure
from netex.models.general_sections_in_frame_rel_structure import GeneralSectionsInFrameRelStructure
from netex.models.group_of_links_in_frame_rel_structure import GroupOfLinksInFrameRelStructure
from netex.models.group_of_links_rel_structure import GroupOfLinksRelStructure
from netex.models.group_of_points_rel_structure import GroupOfPointsRelStructure
from netex.models.groups_of_lines_in_frame_rel_structure import GroupsOfLinesInFrameRelStructure
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.line_networks_in_frame_rel_structure import LineNetworksInFrameRelStructure
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.logical_displays_in_frame_rel_structure import LogicalDisplaysInFrameRelStructure
from netex.models.network import Network
from netex.models.networks_in_frame_rel_structure import NetworksInFrameRelStructure
from netex.models.notice_assignments_in_frame_rel_structure import NoticeAssignmentsInFrameRelStructure
from netex.models.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.models.passenger_information_equipments_in_frame_rel_structure import PassengerInformationEquipmentsInFrameRelStructure
from netex.models.route_links_in_frame_rel_structure import RouteLinksInFrameRelStructure
from netex.models.route_points_in_frame_rel_structure import RoutePointsInFrameRelStructure
from netex.models.routes_in_frame_rel_structure import RoutesInFrameRelStructure
from netex.models.routing_constraint_zones_in_frame_rel_structure import RoutingConstraintZonesInFrameRelStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_exclusions_in_frame_rel_structure import ServiceExclusionsInFrameRelStructure
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.stop_areas_in_frame_rel_structure import StopAreasInFrameRelStructure
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.tariff_zones_in_frame_rel_structure import TariffZonesInFrameRelStructure
from netex.models.time_demand_type_assignments_in_frame_rel_structure import TimeDemandTypeAssignmentsInFrameRelStructure
from netex.models.time_demand_types_in_frame_rel_structure import TimeDemandTypesInFrameRelStructure
from netex.models.timing_links_in_frame_rel_structure import TimingLinksInFrameRelStructure
from netex.models.timing_patterns_in_frame_rel_structure import TimingPatternsInFrameRelStructure
from netex.models.timing_points_in_frame_rel_structure import TimingPointsInFrameRelStructure
from netex.models.transfer_restrictions_in_frame_rel_structure import TransferRestrictionsInFrameRelStructure
from netex.models.transfers_in_frame_rel_structure import TransfersInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "Service_VersionFrameStructure"

    network: Optional[Network] = field(
        default=None,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    additional_networks: Optional[NetworksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "additionalNetworks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    directions: Optional[DirectionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_points: Optional[RoutePointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "routePoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_links: Optional[RouteLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "routeLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routes: Optional[RoutesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_point_properties: Optional[FlexiblePointPropertiesRelStructure] = field(
        default=None,
        metadata={
            "name": "flexiblePointProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_link_properties: Optional[FlexibleLinkPropertiesRelStructure] = field(
        default=None,
        metadata={
            "name": "flexibleLinkProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    common_sections: Optional[CommonSectionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "commonSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_sections: Optional[GeneralSectionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "generalSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_links: Optional[GroupOfLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_points: Optional[GroupOfPointsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lines: Optional[LinesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_lines: Optional[GroupsOfLinesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_displays: Optional[DestinationDisplaysInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "destinationDisplays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_networks: Optional[LineNetworksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "lineNetworks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_points: Optional[ScheduledStopPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "scheduledStopPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_links: Optional[ServiceLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "serviceLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_patterns: Optional[ServicePatternsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "servicePatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_areas: Optional[StopAreasInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "stopAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connections: Optional[TransfersInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zones: Optional[TariffZonesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_assignments: Optional[StopAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "stopAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_points: Optional[TimingPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timingPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_links: Optional[TimingLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timingLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_patterns: Optional[TimingPatternsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timingPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_patterns: Optional[JourneyPatternsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfer_restrictions: Optional[TransferRestrictionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "transferRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routing_constraint_zones: Optional[RoutingConstraintZonesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "routingConstraintZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_exclusions: Optional[ServiceExclusionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "serviceExclusions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_types: Optional[TimeDemandTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_assignments: Optional[TimeDemandTypeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timeDemandTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_link_groups: Optional[GroupOfLinksInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "timingLinkGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notices: Optional[NoticesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    logical_displays: Optional[LogicalDisplaysInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "logicalDisplays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    display_assignments: Optional[DisplayAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "displayAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_information_equipments: Optional[PassengerInformationEquipmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "passengerInformationEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
