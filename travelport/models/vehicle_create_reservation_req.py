from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.action_status_1 import ActionStatus1
from travelport.models.associated_remark_2 import AssociatedRemark2
from travelport.models.base_create_with_form_of_payment_req_1 import (
    BaseCreateWithFormOfPaymentReq1,
)
from travelport.models.booking_source_1 import BookingSource1
from travelport.models.collection_address import CollectionAddress
from travelport.models.delivery_address import DeliveryAddress
from travelport.models.email_1 import Email1
from travelport.models.flight_arrival_information import (
    FlightArrivalInformation,
)
from travelport.models.guarantee_1 import Guarantee1
from travelport.models.payment_information import PaymentInformation
from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.reservation_name_1 import ReservationName1
from travelport.models.review_booking_1 import ReviewBooking1
from travelport.models.special_equipment_1 import SpecialEquipment1
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.vehicle import Vehicle
from travelport.models.vehicle_date_location import VehicleDateLocation
from travelport.models.vehicle_special_request import VehicleSpecialRequest

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class VehicleCreateReservationReq(BaseCreateWithFormOfPaymentReq1):
    """
    Parameters
    ----------
    email
    phone_number
    vehicle_date_location
    vehicle
    special_equipment
    vehicle_special_request
    payment_information
    point_of_sale
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
    reservation_name
        If specified then it will be used for GDS reservation otherwise
        first booking traveler will be used.
    third_party_information
    action_status
    review_booking
        Review Booking or Queue Minders is to add the reminders in the
        Provider Reservation along with the date time and Queue details. On
        the date time defined in reminders, the message along with the PNR
        goes to the desired Queue.
    mandatory_rate_match
        If true, vehicle will not be booked if there is a rate discrepancy.
        Default is false. Supported providers: 1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

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
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    vehicle: None | Vehicle = field(
        default=None,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    special_equipment: list[SpecialEquipment1] = field(
        default_factory=list,
        metadata={
            "name": "SpecialEquipment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 6,
        },
    )
    vehicle_special_request: None | VehicleSpecialRequest = field(
        default=None,
        metadata={
            "name": "VehicleSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    payment_information: None | PaymentInformation = field(
        default=None,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    point_of_sale: None | PointOfSale1 = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    delivery_address: None | DeliveryAddress = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    collection_address: None | CollectionAddress = field(
        default=None,
        metadata={
            "name": "CollectionAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    flight_arrival_information: None | FlightArrivalInformation = field(
        default=None,
        metadata={
            "name": "FlightArrivalInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
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
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
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
    reservation_name: None | ReservationName1 = field(
        default=None,
        metadata={
            "name": "ReservationName",
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
    action_status: None | ActionStatus1 = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    review_booking: list[ReviewBooking1] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    mandatory_rate_match: bool = field(
        default=False,
        metadata={
            "name": "MandatoryRateMatch",
            "type": "Attribute",
        },
    )
