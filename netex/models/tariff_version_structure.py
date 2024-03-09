from dataclasses import dataclass, field
from typing import Optional, Union

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .assistance_booking_service_ref import AssistanceBookingServiceRef
from .assistance_service_ref import AssistanceServiceRef
from .authority_ref import AuthorityRef
from .car_pooling_service_ref import CarPoolingServiceRef
from .catering_service_ref import CateringServiceRef
from .chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from .communication_service_ref import CommunicationServiceRef
from .complaints_service_ref import ComplaintsServiceRef
from .customer_service_ref import CustomerServiceRef
from .distance_matrix_elements_rel_structure import (
    DistanceMatrixElementsRelStructure,
)
from .entity_in_version_structure import DataManagedObjectStructure
from .fare_structure_elements_rel_structure import (
    FareStructureElementsRelStructure,
)
from .flexible_line_ref import FlexibleLineRef
from .general_organisation_ref import GeneralOrganisationRef
from .geographical_intervals_rel_structure import (
    GeographicalIntervalsRelStructure,
)
from .geographical_structure_factors_rel_structure import (
    GeographicalStructureFactorsRelStructure,
)
from .geographical_unit_ref import GeographicalUnitRef
from .group_of_lines_ref import GroupOfLinesRef
from .group_of_operators_ref import GroupOfOperatorsRef
from .groups_of_distance_matrix_elements_rel_structure import (
    GroupsOfDistanceMatrixElementsRelStructure,
)
from .hire_service_ref import HireServiceRef
from .info_links_rel_structure import InfoLinksRelStructure
from .left_luggage_service_ref import LeftLuggageServiceRef
from .line_ref import LineRef
from .local_service_ref import LocalServiceRef
from .lost_property_service_ref import LostPropertyServiceRef
from .luggage_service_ref import LuggageServiceRef
from .management_agent_ref import ManagementAgentRef
from .meeting_point_service_ref import MeetingPointServiceRef
from .money_service_ref import MoneyServiceRef
from .multilingual_string import MultilingualString
from .network_ref import NetworkRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .online_service_operator_ref import OnlineServiceOperatorRef
from .online_service_ref import OnlineServiceRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .price_unit_ref import PriceUnitRef
from .priceable_object_version_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from .private_code import PrivateCode
from .quality_structure_factors_rel_structure import (
    QualityStructureFactorsRelStructure,
)
from .retail_consortium_ref import RetailConsortiumRef
from .retail_service_ref import RetailServiceRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .tariff_basis_enumeration import TariffBasisEnumeration
from .taxi_service_ref import TaxiServiceRef
from .ticketing_service_ref import TicketingServiceRef
from .time_intervals_rel_structure import TimeIntervalsRelStructure
from .time_structure_factors_rel_structure import (
    TimeStructureFactorsRelStructure,
)
from .time_unit_ref import TimeUnitRef
from .travel_agent_ref import TravelAgentRef
from .type_of_tariff_ref import TypeOfTariffRef
from .vehicle_rental_service_ref import VehicleRentalServiceRef
from .vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Tariff_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    document_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            RetailConsortiumRef,
            OnlineServiceOperatorRef,
            GeneralOrganisationRef,
            ManagementAgentRef,
            ServicedOrganisationRef,
            TravelAgentRef,
            OtherOrganisationRef,
            AuthorityRef,
            OperatorRef,
            OrganisationRef,
            GroupOfOperatorsRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineServiceOperatorRef",
                    "type": OnlineServiceOperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    line_ref_or_group_of_lines_ref: Optional[
        Union[FlexibleLineRef, LineRef, NetworkRef, GroupOfLinesRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: Optional[
        Union[
            OnlineServiceRef,
            VehicleRentalServiceRef,
            VehicleSharingServiceRef,
            ChauffeuredVehicleServiceRef,
            TaxiServiceRef,
            CarPoolingServiceRef,
            AssistanceBookingServiceRef,
            CateringServiceRef,
            RetailServiceRef,
            MoneyServiceRef,
            HireServiceRef,
            CommunicationServiceRef,
            MeetingPointServiceRef,
            LeftLuggageServiceRef,
            LuggageServiceRef,
            LostPropertyServiceRef,
            ComplaintsServiceRef,
            CustomerServiceRef,
            AssistanceServiceRef,
            TicketingServiceRef,
            LocalServiceRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingServiceRef",
                    "type": AssistanceBookingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringServiceRef",
                    "type": CateringServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailServiceRef",
                    "type": RetailServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyServiceRef",
                    "type": MoneyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireServiceRef",
                    "type": HireServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationServiceRef",
                    "type": CommunicationServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointServiceRef",
                    "type": MeetingPointServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageServiceRef",
                    "type": LeftLuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageServiceRef",
                    "type": LuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyServiceRef",
                    "type": LostPropertyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsServiceRef",
                    "type": ComplaintsServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerServiceRef",
                    "type": CustomerServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceServiceRef",
                    "type": AssistanceServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingServiceRef",
                    "type": TicketingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LocalServiceRef",
                    "type": LocalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_tariff_ref: Optional[TypeOfTariffRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_basis: Optional[TariffBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "TariffBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    return_fare_twice_single: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnFareTwiceSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_intervals: Optional[GeographicalIntervalsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "geographicalIntervals",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    geographical_structure_factors: Optional[
        GeographicalStructureFactorsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "geographicalStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_intervals: Optional[TimeIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_structure_factors: Optional[TimeStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quality_structure_factors: Optional[
        QualityStructureFactorsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "qualityStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_structure_elements: Optional[FareStructureElementsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "fareStructureElements",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    distance_matrix_elements: Optional[DistanceMatrixElementsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "distanceMatrixElements",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    groups_of_distance_matrix_elements: Optional[
        GroupsOfDistanceMatrixElementsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "groupsOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
