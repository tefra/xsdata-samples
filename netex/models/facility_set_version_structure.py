from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

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


@dataclass
class FacilitySetVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "FacilitySet_VersionStructure"

    provided_by_ref: OrganisationRefStructure | None = field(
        default=None,
        metadata={
            "name": "ProvidedByRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_facility_ref: TypeOfFacilityRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    other_facilities: TypesOfEquipmentRelStructure | None = field(
        default=None,
        metadata={
            "name": "otherFacilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_info_facility_list: AccessibilityInfoFacilityList | None = field(
        default=None,
        metadata={
            "name": "AccessibilityInfoFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assistance_facility_list: AssistanceFacilityList | None = field(
        default=None,
        metadata={
            "name": "AssistanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_tool_list: AccessibilityToolList | None = field(
        default=None,
        metadata={
            "name": "AccessibilityToolList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    car_service_facility_list: CarServiceFacilityList | None = field(
        default=None,
        metadata={
            "name": "CarServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    catering_facility_list: CateringFacilityList | None = field(
        default=None,
        metadata={
            "name": "CateringFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    family_facility_list: FamilyFacilityList | None = field(
        default=None,
        metadata={
            "name": "FamilyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_classes: FareClasses | None = field(
        default=None,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender_limitation: GenderLimitation | None = field(
        default=None,
        metadata={
            "name": "GenderLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    meal_facility_list: MealFacilityList | None = field(
        default=None,
        metadata={
            "name": "MealFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medical_facility_list: MedicalFacilityList | None = field(
        default=None,
        metadata={
            "name": "MedicalFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobility_facility_list: MobilityFacilityList | None = field(
        default=None,
        metadata={
            "name": "MobilityFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    nuisance_facility_list: NuisanceFacilityList | None = field(
        default=None,
        metadata={
            "name": "NuisanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_comms_facility_list: PassengerCommsFacilityList | None = (
        field(
            default=None,
            metadata={
                "name": "PassengerCommsFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    passenger_information_equipment_list: Iterable[
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
    passenger_information_facility_list: PassengerInformationFacilityList | None = field(
        default=None,
        metadata={
            "name": "PassengerInformationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_facility_list: RetailFacilityList | None = field(
        default=None,
        metadata={
            "name": "RetailFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    safety_facility_list: SafetyFacilityList | None = field(
        default=None,
        metadata={
            "name": "SafetyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sanitary_facility_list: SanitaryFacilityList | None = field(
        default=None,
        metadata={
            "name": "SanitaryFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_facility_list: TicketingFacilityList | None = field(
        default=None,
        metadata={
            "name": "TicketingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_service_facility_list: TicketingServiceFacilityList | None = (
        field(
            default=None,
            metadata={
                "name": "TicketingServiceFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
