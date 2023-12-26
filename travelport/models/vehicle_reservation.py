from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.associated_remark_2 import AssociatedRemark2
from travelport.models.base_reservation_1 import BaseReservation1
from travelport.models.booking_source_1 import BookingSource1
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.collection_address import CollectionAddress
from travelport.models.delivery_address import DeliveryAddress
from travelport.models.email_1 import Email1
from travelport.models.flight_arrival_information import (
    FlightArrivalInformation,
)
from travelport.models.guarantee_1 import Guarantee1
from travelport.models.payment_information import PaymentInformation
from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.reservation_name_1 import ReservationName1
from travelport.models.special_equipment_1 import SpecialEquipment1
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.vehicle import Vehicle
from travelport.models.vehicle_date_location import VehicleDateLocation
from travelport.models.vehicle_special_request import VehicleSpecialRequest

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleReservation(BaseReservation1):
    """
    Parameters
    ----------
    booking_traveler_ref
    reservation_name
    email
    phone_number
    vehicle_date_location
    vehicle
    special_equipment
    vehicle_special_request
    payment_information
    delivery_address
        An address to which a rental car should be delivered and a phone
        number associated with the address.
    collection_address
        An address from which a rental car should be picked up at the end of
        a rental period and a phone number associated with the address.
    flight_arrival_information
        The flight arrival information (airline code and flight number) for
        the airport/city at which the rental car will be picked up
    guarantee
    associated_remark
    booking_source
        Specify alternate booking source
    third_party_information
    sell_message
    supplier_code
    booking_confirmation
    status
    provider_reservation_info_ref
        Provider reservation reference key.
    passive_provider_reservation_info_ref
        Passive Provider reservation reference key.
    travel_order
        To identify the appropriate sequence for Air/Car/Hotel segments
        based on travel dates.
    provider_segment_order
        To identify the appropriate travel sequence for Air/Car/Hotel/Rail
        segments/reservations in the provider reservation.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
    email: list[Email1] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    phone_number: list[PhoneNumber1] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    vehicle_date_location: None | VehicleDateLocation = field(
        default=None,
        metadata={
            "name": "VehicleDateLocation",
            "type": "Element",
            "required": True,
        },
    )
    vehicle: None | Vehicle = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "required": True,
        },
    )
    special_equipment: list[SpecialEquipment1] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        },
    )
    vehicle_special_request: None | VehicleSpecialRequest = field(
        default=None,
        metadata={
            "name": "VehicleSpecialRequest",
            "type": "Element",
        },
    )
    payment_information: None | PaymentInformation = field(
        default=None,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
        },
    )
    delivery_address: None | DeliveryAddress = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
        },
    )
    collection_address: None | CollectionAddress = field(
        default=None,
        metadata={
            "name": "CollectionAddress",
            "type": "Element",
        },
    )
    flight_arrival_information: None | FlightArrivalInformation = field(
        default=None,
        metadata={
            "name": "FlightArrivalInformation",
            "type": "Element",
        },
    )
    guarantee: None | Guarantee1 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    associated_remark: list[AssociatedRemark2] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    booking_source: None | BookingSource1 = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    third_party_information: None | ThirdPartyInformation1 = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    sell_message: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SellMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
        },
    )
    booking_confirmation: None | str = field(
        default=None,
        metadata={
            "name": "BookingConfirmation",
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
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    passive_provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    travel_order: None | int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        },
    )
    provider_segment_order: None | int = field(
        default=None,
        metadata={
            "name": "ProviderSegmentOrder",
            "type": "Attribute",
            "max_inclusive": 999,
        },
    )
