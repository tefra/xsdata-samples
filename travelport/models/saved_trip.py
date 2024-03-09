from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from travelport.models.accounting_remark_1 import AccountingRemark1
from travelport.models.agency_contact_info_1 import AgencyContactInfo1
from travelport.models.agency_info_1 import AgencyInfo1
from travelport.models.air_pricing_modifiers import AirPricingModifiers
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.booking_traveler_1 import BookingTraveler1
from travelport.models.collection_address import CollectionAddress
from travelport.models.delivery_address import DeliveryAddress
from travelport.models.flight_arrival_information import (
    FlightArrivalInformation,
)
from travelport.models.general_remark_1 import GeneralRemark1
from travelport.models.hotel_details_modifiers import HotelDetailsModifiers
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail
from travelport.models.hotel_rules_modifiers import HotelRulesModifiers
from travelport.models.hotel_stay import HotelStay
from travelport.models.payment_information import PaymentInformation
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.policy_information_2 import PolicyInformation2
from travelport.models.profile_association import ProfileAssociation
from travelport.models.promotion_code import PromotionCode
from travelport.models.rail_fare_note import RailFareNote
from travelport.models.rail_pricing_solution import RailPricingSolution
from travelport.models.reservation_name_1 import ReservationName1
from travelport.models.saved_trip_activity import SavedTripActivity
from travelport.models.search_passenger_1 import SearchPassenger1
from travelport.models.special_equipment_1 import SpecialEquipment1
from travelport.models.type_saved_trip_note import TypeSavedTripNote
from travelport.models.vehicle import Vehicle
from travelport.models.vehicle_date_location import VehicleDateLocation
from travelport.models.vehicle_search_modifiers import VehicleSearchModifiers
from travelport.models.vehicle_special_request import VehicleSpecialRequest
from travelport.models.vendor_location_1 import VendorLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTrip:
    """
    SavedTrip holds a draft Itinerary/booking which can be used at later point of
    time to do a booking.

    Parameters
    ----------
    booking_traveler
    agency_contact_info
    search_passenger
    point_of_sale
    accounting_remark
    general_remark
    agency_info
    reservation_name
    air_pricing_modifiers
    air_pricing_solution
    air_trip_note
    vehicle_search_modifiers
    vehicle_date_location
    special_equipment
    vehicle_special_request
    payment_information
    delivery_address
    collection_address
    flight_arrival_information
    vehicle
    vehicle_trip_note
    vendor_location
    hotel_property
    hotel_stay
    hotel_rules_modifiers
    hotel_details_modifiers
    hotel_rate_detail
    promotion_code
    hotel_trip_note
    rail_pricing_solution
    rail_fare_note
    rail_trip_note
    saved_trip_note
    saved_trip_activity
    profile_association
    policy_information
    locator_code
        Alpha numeric String to identify a SavedTrip uniquely.
    universal_record_locator_code
        Alpha numeric String to identify a the UniversalRecord created using
        this SavedTrip.
    name
        Name of the Saved Trip.
    create_date
        The date and time that this SavedTrip was created.
    modified_date
        The date and time that this SavedTrip was Modified.
    version
    status
    created_by_agent
        The Agent Code who created the SavedTrip.
    modified_by_agent
        The Agent Code that modified the SavedTrip.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_traveler: list[BookingTraveler1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    agency_contact_info: None | AgencyContactInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    search_passenger: list[SearchPassenger1] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    point_of_sale: list[PointOfSale1] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    accounting_remark: list[AccountingRemark1] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    general_remark: list[GeneralRemark1] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    agency_info: None | AgencyInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    reservation_name: None | ReservationName1 = field(
        default=None,
        metadata={
            "name": "ReservationName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    air_pricing_modifiers: list[AirPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    air_trip_note: list[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "AirTripNote",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    vehicle_search_modifiers: list[VehicleSearchModifiers] = field(
        default_factory=list,
        metadata={
            "name": "VehicleSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    vehicle_date_location: list[VehicleDateLocation] = field(
        default_factory=list,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    special_equipment: list[SpecialEquipment1] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    vehicle_special_request: list[VehicleSpecialRequest] = field(
        default_factory=list,
        metadata={
            "name": "VehicleSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    payment_information: list[PaymentInformation] = field(
        default_factory=list,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    delivery_address: list[DeliveryAddress] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    collection_address: list[CollectionAddress] = field(
        default_factory=list,
        metadata={
            "name": "CollectionAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    flight_arrival_information: list[FlightArrivalInformation] = field(
        default_factory=list,
        metadata={
            "name": "FlightArrivalInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    vehicle: list[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    vehicle_trip_note: list[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTripNote",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    vendor_location: list[VendorLocation1] = field(
        default_factory=list,
        metadata={
            "name": "VendorLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_property: list[HotelProperty] = field(
        default_factory=list,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_stay: list[HotelStay] = field(
        default_factory=list,
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_rules_modifiers: list[HotelRulesModifiers] = field(
        default_factory=list,
        metadata={
            "name": "HotelRulesModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_details_modifiers: list[HotelDetailsModifiers] = field(
        default_factory=list,
        metadata={
            "name": "HotelDetailsModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_rate_detail: list[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    promotion_code: list[PromotionCode] = field(
        default_factory=list,
        metadata={
            "name": "PromotionCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_trip_note: list[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "HotelTripNote",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    rail_pricing_solution: list[RailPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        },
    )
    rail_fare_note: list[RailFareNote] = field(
        default_factory=list,
        metadata={
            "name": "RailFareNote",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        },
    )
    rail_trip_note: list[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "RailTripNote",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    saved_trip_note: list[TypeSavedTripNote] = field(
        default_factory=list,
        metadata={
            "name": "SavedTripNote",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    saved_trip_activity: list[SavedTripActivity] = field(
        default_factory=list,
        metadata={
            "name": "SavedTripActivity",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    profile_association: list[ProfileAssociation] = field(
        default_factory=list,
        metadata={
            "name": "ProfileAssociation",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    policy_information: None | PolicyInformation2 = field(
        default=None,
        metadata={
            "name": "PolicyInformation",
            "type": "Element",
        },
    )
    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 50,
        },
    )
    create_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
        },
    )
    modified_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    created_by_agent: None | str = field(
        default=None,
        metadata={
            "name": "CreatedByAgent",
            "type": "Attribute",
        },
    )
    modified_by_agent: None | str = field(
        default=None,
        metadata={
            "name": "ModifiedByAgent",
            "type": "Attribute",
        },
    )
