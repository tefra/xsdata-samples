from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.accessibility_enum import AccessibilityEnum
from datexii.models.eu.datexii.v2.availability_enum import AvailabilityEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.opening_times import OpeningTimes
from datexii.models.eu.datexii.v2.tariffs_and_payment import TariffsAndPayment
from datexii.models.eu.datexii.v2.user_type_enum import UserTypeEnum
from datexii.models.eu.datexii.v2.vehicle_characteristics import VehicleCharacteristics

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingEquipmentOrServiceFacility:
    """
    One type of equipment or additional service facility that is available at the
    parking site, parking space or group of parking spaces.

    :ivar equipment_or_service_facility_identifier: An internal
        identifier for the equipment or service facility, e.g. an
        inventory number. This attribute has an unbounded multiplicity
        to support identifiers for multiple occurrences of this element.
    :ivar availability: Specifies, if the element in question is
        available or not. Note that this is no dynamic information!
    :ivar number_of_equipment_or_service_facility: Number of the
        specified element (e.g. number of toilets, restaurants, park
        &amp; ride places, etc.) with respect to user restriction for
        the parking record, a complete group of spaces or a single
        space. Dynamic overridable.
    :ivar additional_description: Provides an additional description.
    :ivar other_equipment_or_service_facility: Specifies the additional
        equipment or service facility, if the enumerations provided do
        not fit. Use literal 'other' in this case.
    :ivar accessibility: Information on accessibility, easements and
        marking for handicapped people.
    :ivar name_or_brand: Name or brand of the equipment or service
        facility, e.g. brand of petrol station, name of the WC-Service
        etc.
    :ivar comment: A free text comment that can be used by the operator
        to convey un-coded observations/information.
    :ivar photo_url: Specifies a URL at which a photo of the object in
        concern can be found.
    :ivar applicable_for_user: Limitation to a set of special users.
    :ivar availability_and_opening_times: Specify the general
        availability of some equipment or service facility (by using
        just the 'OverallPeriod' component) or specify its opening times
        more detailed.
    :ivar tariffs_and_payment:
    :ivar group_of_locations:
    :ivar applicable_for_vehicles:
    :ivar parking_equipment_or_service_facility_extension:
    """
    equipment_or_service_facility_identifier: List[str] = field(
        default_factory=list,
        metadata={
            "name": "equipmentOrServiceFacilityIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    availability: Optional[AvailabilityEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    number_of_equipment_or_service_facility: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    additional_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "additionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_equipment_or_service_facility: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "otherEquipmentOrServiceFacility",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    accessibility: List[AccessibilityEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    name_or_brand: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "nameOrBrand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    photo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "photoUrl",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_user: List[UserTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForUser",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    availability_and_opening_times: Optional[OpeningTimes] = field(
        default=None,
        metadata={
            "name": "availabilityAndOpeningTimes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    tariffs_and_payment: Optional[TariffsAndPayment] = field(
        default=None,
        metadata={
            "name": "tariffsAndPayment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    applicable_for_vehicles: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "applicableForVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    parking_equipment_or_service_facility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingEquipmentOrServiceFacilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
