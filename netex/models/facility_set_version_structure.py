from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.accessibility_info_facility_enumeration import AccessibilityInfoFacilityEnumeration
from netex.models.accessibility_tool_enumeration import AccessibilityToolEnumeration
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.assistance_facility_enumeration import AssistanceFacilityEnumeration
from netex.models.car_service_facility_enumeration import CarServiceFacilityEnumeration
from netex.models.catering_facility_enumeration import CateringFacilityEnumeration
from netex.models.family_facility_enumeration import FamilyFacilityEnumeration
from netex.models.fare_class_enumeration import FareClassEnumeration
from netex.models.gender_limitation_enumeration import GenderLimitationEnumeration
from netex.models.meal_facility_enumeration import MealFacilityEnumeration
from netex.models.medical_facility_enumeration import MedicalFacilityEnumeration
from netex.models.mobility_facility_enumeration import MobilityFacilityEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration
from netex.models.passenger_information_equipment_enumeration import PassengerInformationEquipmentEnumeration
from netex.models.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration
from netex.models.retail_facility_enumeration import RetailFacilityEnumeration
from netex.models.safety_facility_enumeration import SafetyFacilityEnumeration
from netex.models.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from netex.models.ticketing_facility_enumeration import TicketingFacilityEnumeration
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.type_of_facility_ref import TypeOfFacilityRef
from netex.models.types_of_equipment_rel_structure import TypesOfEquipmentRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FacilitySetVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "FacilitySet_VersionStructure"

    provided_by_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "ProvidedByRef",
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
    type_of_facility_ref: Optional[TypeOfFacilityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_facilities: Optional[TypesOfEquipmentRelStructure] = field(
        default=None,
        metadata={
            "name": "otherFacilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_info_facility_list: List[AccessibilityInfoFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityInfoFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    assistance_facility_list: List[AssistanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AssistanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    accessibility_tool_list: List[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityToolList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    car_service_facility_list: List[CarServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "CarServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    catering_facility_list: List[CateringFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "CateringFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    family_facility_list: List[FamilyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FamilyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    fare_classes: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    gender_limitation: Optional[GenderLimitationEnumeration] = field(
        default=None,
        metadata={
            "name": "GenderLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    meal_facility_list: List[MealFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MealFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    medical_facility_list: List[MedicalFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MedicalFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    mobility_facility_list: List[MobilityFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MobilityFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    nuisance_facility_list: List[NuisanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "NuisanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    passenger_comms_facility_list: List[PassengerCommsFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCommsFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    passenger_information_equipment_list: Optional[PassengerInformationEquipmentEnumeration] = field(
        default=None,
        metadata={
            "name": "PassengerInformationEquipmentList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_information_facility_list: List[PassengerInformationFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    retail_facility_list: List[RetailFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RetailFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    safety_facility_list: List[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SafetyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    sanitary_facility_list: List[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticketing_facility_list: List[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    ticketing_service_facility_list: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
