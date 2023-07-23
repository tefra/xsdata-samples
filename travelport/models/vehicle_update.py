from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.associated_remark_2 import AssociatedRemark2
from travelport.models.booking_source_1 import BookingSource1
from travelport.models.collection_address import CollectionAddress
from travelport.models.delivery_address import DeliveryAddress
from travelport.models.drivers_license_1 import DriversLicense1
from travelport.models.flight_arrival_information import FlightArrivalInformation
from travelport.models.guarantee_1 import Guarantee1
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.payment_information import PaymentInformation
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.travel_compliance_data_1 import TravelComplianceData1
from travelport.models.vehicle_pickup_date_location import VehiclePickupDateLocation
from travelport.models.vehicle_rate_info import VehicleRateInfo
from travelport.models.vehicle_return_date_location import VehicleReturnDateLocation
from travelport.models.vehicle_special_request import VehicleSpecialRequest
from travelport.models.vehicle_type_identifier import VehicleTypeIdentifier

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class VehicleUpdate:
    """
    Parameters
    ----------
    loyalty_card
    drivers_license
    guarantee
    booking_source
    vehicle_rate_info
    payment_information
    associated_remark
    vehicle_special_request
    delivery_address
    collection_address
    vehicle_return_date_location
    vehicle_pickup_date_location
    third_party_information
        Third party supplier locator information. Specifically applicable
        for SDK booking. Previously saved values can be updated for
        SupplierCode, SupplierName and SupplierLocatorCode. If an attribute
        is not passed here, then previously saved value for that attribute
        will be deleted.
    travel_compliance_data
    vehicle_type_identifier
    flight_arrival_information
        The flight arrival information(airline code and flight number) for
        the airport/city at which the rental car will be picked up ||
        Addition and Update in UR Modify is currently implemented only for
        Galileo(1G) and Apollo(1V).
    reservation_locator_code
    booking_traveler_ref
        BookingTravelerRef will be used to specify BookingTraveler in UR.
        Currently this will be used to LoyaltyCard modification. Later this
        can used for other elements which are associated with
        BookngTraveler.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    drivers_license: None | DriversLicense1 = field(
        default=None,
        metadata={
            "name": "DriversLicense",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    guarantee: None | Guarantee1 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    booking_source: None | BookingSource1 = field(
        default=None,
        metadata={
            "name": "BookingSource",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    vehicle_rate_info: None | VehicleRateInfo = field(
        default=None,
        metadata={
            "name": "VehicleRateInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    payment_information: None | PaymentInformation = field(
        default=None,
        metadata={
            "name": "PaymentInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    associated_remark: list[AssociatedRemark2] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_special_request: None | VehicleSpecialRequest = field(
        default=None,
        metadata={
            "name": "VehicleSpecialRequest",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    delivery_address: None | DeliveryAddress = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    collection_address: None | CollectionAddress = field(
        default=None,
        metadata={
            "name": "CollectionAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    vehicle_return_date_location: None | VehicleReturnDateLocation = field(
        default=None,
        metadata={
            "name": "VehicleReturnDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    vehicle_pickup_date_location: None | VehiclePickupDateLocation = field(
        default=None,
        metadata={
            "name": "VehiclePickupDateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    third_party_information: None | ThirdPartyInformation1 = field(
        default=None,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    travel_compliance_data: list[TravelComplianceData1] = field(
        default_factory=list,
        metadata={
            "name": "TravelComplianceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    vehicle_type_identifier: None | VehicleTypeIdentifier = field(
        default=None,
        metadata={
            "name": "VehicleTypeIdentifier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    flight_arrival_information: None | FlightArrivalInformation = field(
        default=None,
        metadata={
            "name": "FlightArrivalInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        }
    )
    reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        }
    )
