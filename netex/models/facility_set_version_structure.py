from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .accessibility_info_facility_list import AccessibilityInfoFacilityList
from .accessibility_tool_list import AccessibilityToolList
from .assistance_facility_list import AssistanceFacilityList
from .car_service_facility_list import CarServiceFacilityList
from .catering_facility_list import CateringFacilityList
from .entity_in_version_structure import DataManagedObjectStructure
from .family_facility_list import FamilyFacilityList
from .fare_classes import FareClasses
from .gender_limitation import GenderLimitation
from .meal_facility_list import MealFacilityList
from .medical_facility_list import MedicalFacilityList
from .mobility_facility_list import MobilityFacilityList
from .multilingual_string import MultilingualString
from .nuisance_facility_list import NuisanceFacilityList
from .organisation_ref_structure import OrganisationRefStructure
from .passenger_comms_facility_list import PassengerCommsFacilityList
from .passenger_information_equipment_enumeration import (
    PassengerInformationEquipmentEnumeration,
)
from .passenger_information_facility_list import (
    PassengerInformationFacilityList,
)
from .retail_facility_list import RetailFacilityList
from .safety_facility_list import SafetyFacilityList
from .sanitary_facility_list import SanitaryFacilityList
from .ticketing_facility_list import TicketingFacilityList
from .ticketing_service_facility_list import TicketingServiceFacilityList
from .type_of_facility_ref import TypeOfFacilityRef
from .types_of_equipment_rel_structure import TypesOfEquipmentRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilitySetVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "FacilitySet_VersionStructure"

    provided_by_ref: None | OrganisationRefStructure = field(
        default=None,
        metadata={
            "name": "ProvidedByRef",
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
    type_of_facility_ref: None | TypeOfFacilityRef = field(
        default=None,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    other_facilities: None | TypesOfEquipmentRelStructure = field(
        default=None,
        metadata={
            "name": "otherFacilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_info_facility_list: None | AccessibilityInfoFacilityList = (
        field(
            default=None,
            metadata={
                "name": "AccessibilityInfoFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    assistance_facility_list: None | AssistanceFacilityList = field(
        default=None,
        metadata={
            "name": "AssistanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_tool_list: None | AccessibilityToolList = field(
        default=None,
        metadata={
            "name": "AccessibilityToolList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    car_service_facility_list: None | CarServiceFacilityList = field(
        default=None,
        metadata={
            "name": "CarServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    catering_facility_list: None | CateringFacilityList = field(
        default=None,
        metadata={
            "name": "CateringFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    family_facility_list: None | FamilyFacilityList = field(
        default=None,
        metadata={
            "name": "FamilyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_classes: None | FareClasses = field(
        default=None,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender_limitation: None | GenderLimitation = field(
        default=None,
        metadata={
            "name": "GenderLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    meal_facility_list: None | MealFacilityList = field(
        default=None,
        metadata={
            "name": "MealFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medical_facility_list: None | MedicalFacilityList = field(
        default=None,
        metadata={
            "name": "MedicalFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobility_facility_list: None | MobilityFacilityList = field(
        default=None,
        metadata={
            "name": "MobilityFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    nuisance_facility_list: None | NuisanceFacilityList = field(
        default=None,
        metadata={
            "name": "NuisanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_comms_facility_list: None | PassengerCommsFacilityList = field(
        default=None,
        metadata={
            "name": "PassengerCommsFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_information_equipment_list: Sequence[
        PassengerInformationEquipmentEnumeration
    ] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationEquipmentList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    passenger_information_facility_list: (
        None | PassengerInformationFacilityList
    ) = field(
        default=None,
        metadata={
            "name": "PassengerInformationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_facility_list: None | RetailFacilityList = field(
        default=None,
        metadata={
            "name": "RetailFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    safety_facility_list: None | SafetyFacilityList = field(
        default=None,
        metadata={
            "name": "SafetyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sanitary_facility_list: None | SanitaryFacilityList = field(
        default=None,
        metadata={
            "name": "SanitaryFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_facility_list: None | TicketingFacilityList = field(
        default=None,
        metadata={
            "name": "TicketingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_service_facility_list: None | TicketingServiceFacilityList = (
        field(
            default=None,
            metadata={
                "name": "TicketingServiceFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
