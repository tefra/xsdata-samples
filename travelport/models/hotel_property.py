from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.amenities import Amenities
from travelport.models.coordinate_location_1 import CoordinateLocation1
from travelport.models.distance_1 import Distance1
from travelport.models.hotel_rating import HotelRating
from travelport.models.marketing_message import MarketingMessage
from travelport.models.phone_number_1 import PhoneNumber1
from travelport.models.type_hotel_availability import TypeHotelAvailability
from travelport.models.type_net_trans_commission import TypeNetTransCommission
from travelport.models.type_reserve_requirement import TypeReserveRequirement
from travelport.models.type_unstructured_address import TypeUnstructuredAddress

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelProperty:
    """
    The hotel property.

    Parameters
    ----------
    property_address
    phone_number
    coordinate_location
    distance
    hotel_rating
    amenities
    marketing_message
    hotel_chain
    hotel_code
    hotel_location
        The location code for this entity. IATA code.
    name
    vendor_location_key
        The VendorLocationKey for this HotelProperty.
    hotel_transportation
        OTA Transporation code. Transportation available to hotel.
    reserve_requirement
    participation_level
        2=Best Available Rate 1G, 1V,  4=Lowest Possible Rate 1G, 1V, 1P
    availability
    key
    preferred_option
        This attribute is used to indicate if the vendors responsible for
        the fare or rate being returned have been determined to be
        ‘preferred’ based on the associated policy settings.
    more_rates
        When true, more rates are available for this hotel
        property.Applicable only for HotelDetails and HotelSuperShopper.
        Supported Providers: 1G, 1V.
    more_rates_token
        HS3 Token to identify the Rates for a property. Supported Providers
        1G,1V.
    net_trans_commission_ind
        This attribute indicates whether hotel property is tracking through
        net trans commission indicator.
    num_of_rate_plans
        The specific number of RatePlanTypes for each property responded on
        the message, integer 1 - 999. Supported provider: HotelSuperShopper
        message only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    property_address: None | TypeUnstructuredAddress = field(
        default=None,
        metadata={
            "name": "PropertyAddress",
            "type": "Element",
        }
    )
    phone_number: list[PhoneNumber1] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    coordinate_location: None | CoordinateLocation1 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    distance: None | Distance1 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    hotel_rating: list[HotelRating] = field(
        default_factory=list,
        metadata={
            "name": "HotelRating",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    amenities: None | Amenities = field(
        default=None,
        metadata={
            "name": "Amenities",
            "type": "Element",
        }
    )
    marketing_message: None | MarketingMessage = field(
        default=None,
        metadata={
            "name": "MarketingMessage",
            "type": "Element",
        }
    )
    hotel_chain: None | str = field(
        default=None,
        metadata={
            "name": "HotelChain",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    hotel_code: None | str = field(
        default=None,
        metadata={
            "name": "HotelCode",
            "type": "Attribute",
            "required": True,
            "max_length": 32,
        }
    )
    hotel_location: None | str = field(
        default=None,
        metadata={
            "name": "HotelLocation",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 6,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    vendor_location_key: None | str = field(
        default=None,
        metadata={
            "name": "VendorLocationKey",
            "type": "Attribute",
        }
    )
    hotel_transportation: None | int = field(
        default=None,
        metadata={
            "name": "HotelTransportation",
            "type": "Attribute",
        }
    )
    reserve_requirement: None | TypeReserveRequirement = field(
        default=None,
        metadata={
            "name": "ReserveRequirement",
            "type": "Attribute",
        }
    )
    participation_level: None | str = field(
        default=None,
        metadata={
            "name": "ParticipationLevel",
            "type": "Attribute",
            "length": 1,
        }
    )
    availability: None | TypeHotelAvailability = field(
        default=None,
        metadata={
            "name": "Availability",
            "type": "Attribute",
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    preferred_option: None | bool = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        }
    )
    more_rates: None | bool = field(
        default=None,
        metadata={
            "name": "MoreRates",
            "type": "Attribute",
        }
    )
    more_rates_token: None | str = field(
        default=None,
        metadata={
            "name": "MoreRatesToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        }
    )
    net_trans_commission_ind: None | TypeNetTransCommission = field(
        default=None,
        metadata={
            "name": "NetTransCommissionInd",
            "type": "Attribute",
        }
    )
    num_of_rate_plans: None | int = field(
        default=None,
        metadata={
            "name": "NumOfRatePlans",
            "type": "Attribute",
        }
    )
