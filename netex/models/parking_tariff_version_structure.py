from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .authority_ref import AuthorityRef
from .entity_in_version_structure import DataManagedObjectStructure
from .general_organisation_ref import GeneralOrganisationRef
from .group_of_operators_ref import GroupOfOperatorsRef
from .info_links_rel_structure import InfoLinksRelStructure
from .management_agent_ref import ManagementAgentRef
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .online_service_operator_ref import OnlineServiceOperatorRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .parking_charge_bands_rel_structure import ParkingChargeBandsRelStructure
from .parking_refs_rel_structure import ParkingRefsRelStructure
from .parking_stay_enumeration import ParkingStayEnumeration
from .parking_user_enumeration import ParkingUserEnumeration
from .parking_vehicle_enumeration import ParkingVehicleEnumeration
from .price_unit_ref import PriceUnitRef
from .priceable_object_version_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from .quality_structure_factors_rel_structure import (
    QualityStructureFactorsRelStructure,
)
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .time_intervals_rel_structure import TimeIntervalsRelStructure
from .time_structure_factors_rel_structure import (
    TimeStructureFactorsRelStructure,
)
from .time_unit_ref import TimeUnitRef
from .transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from .travel_agent_ref import TravelAgentRef
from .type_of_tariff_ref import TypeOfTariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingTariffVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ParkingTariff_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: None | AlternativeNamesRelStructure = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: None | NoticeAssignmentsRelStructure = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    document_links: None | InfoLinksRelStructure = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: (
        None
        | RetailConsortiumRef
        | OnlineServiceOperatorRef
        | GeneralOrganisationRef
        | ManagementAgentRef
        | ServicedOrganisationRef
        | TravelAgentRef
        | OtherOrganisationRef
        | AuthorityRef
        | OperatorRef
        | OrganisationRef
        | GroupOfOperatorsRef
    ) = field(
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
    time_unit_ref: None | TimeUnitRef = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_intervals: None | TimeIntervalsRelStructure = field(
        default=None,
        metadata={
            "name": "timeIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_structure_factors: None | TimeStructureFactorsRelStructure = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quality_structure_factors: None | QualityStructureFactorsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "qualityStructureFactors",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    parking_user_type: None | ParkingUserEnumeration = field(
        default=None,
        metadata={
            "name": "ParkingUserType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_stay_type: None | ParkingStayEnumeration = field(
        default=None,
        metadata={
            "name": "ParkingStayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_vehicle_types: Sequence[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    vehicle_types: None | TransportTypeRefsRelStructure = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    applies_to: None | ParkingRefsRelStructure = field(
        default=None,
        metadata={
            "name": "appliesTo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_tariff_ref: None | TypeOfTariffRef = field(
        default=None,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    additional_tax: None | bool = field(
        default=None,
        metadata={
            "name": "AdditionalTax",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_charge_bands: None | ParkingChargeBandsRelStructure = field(
        default=None,
        metadata={
            "name": "parkingChargeBands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_unit_ref: None | PriceUnitRef = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_groups: None | PriceGroupsRelStructure = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: None | FareTablesRelStructure = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
