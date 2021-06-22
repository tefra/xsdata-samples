from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .authority_ref import AuthorityRef
from .cell_versioned_child_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from .general_organisation_ref import GeneralOrganisationRef
from .group_of_operators_ref import GroupOfOperatorsRef
from .info_links_rel_structure import InfoLinksRelStructure
from .management_agent_ref import ManagementAgentRef
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .parking_charge_bands_rel_structure import ParkingChargeBandsRelStructure
from .parking_refs_rel_structure import ParkingRefsRelStructure
from .parking_stay_enumeration import ParkingStayEnumeration
from .parking_user_enumeration import ParkingUserEnumeration
from .parking_vehicle_enumeration import ParkingVehicleEnumeration
from .price_unit_ref import PriceUnitRef
from .quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .time_intervals_rel_structure import TimeIntervalsRelStructure
from .time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from .time_unit_ref import TimeUnitRef
from .transport_organisation_ref import TransportOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .type_of_tariff_ref import TypeOfTariffRef
from .vehicle_type_refs_rel_structure import VehicleTypeRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingTariffVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ParkingTariff_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    document_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
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
                    "name": "TransportOrganisationRef",
                    "type": TransportOrganisationRef,
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
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitRef",
                    "type": TimeUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeIntervals",
                    "type": TimeIntervalsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeStructureFactors",
                    "type": TimeStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "qualityStructureFactors",
                    "type": QualityStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingUserType",
                    "type": ParkingUserEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingStayType",
                    "type": ParkingStayEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingVehicleTypes",
                    "type": List[ParkingVehicleEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "vehicleTypes",
                    "type": VehicleTypeRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "appliesTo",
                    "type": ParkingRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariffRef",
                    "type": TypeOfTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdditionalTax",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "parkingChargeBands",
                    "type": ParkingChargeBandsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceUnitRef",
                    "type": PriceUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "priceGroups",
                    "type": PriceGroupsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareTables",
                    "type": FareTablesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 62,
        }
    )
