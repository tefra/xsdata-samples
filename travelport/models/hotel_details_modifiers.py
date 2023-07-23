from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_guest_information import BookingGuestInformation
from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.hotel_bedding import HotelBedding
from travelport.models.hotel_stay import HotelStay
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.number_of_children import NumberOfChildren
from travelport.models.permitted_providers_1 import PermittedProviders1
from travelport.models.type_rate_rule_detail import TypeRateRuleDetail

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelDetailsModifiers:
    """
    Controls and switches for the Hotel Details request.

    Parameters
    ----------
    permitted_providers
    loyalty_card
    corporate_discount_id
        Search with corporate discount IDs or negotiated rate codes. 1G/1V
        allows a max of 4.  1P allows a max of 1 corporate discount ID and
        up to 30 negotiated rate codes.  Support for this function is hotel
        supplier dependent.
    hotel_stay
    number_of_children
    hotel_bedding
    rate_category
        Specify Rate Category
    booking_guest_information
        Information about requested rooms and allocation of guests per room.
    number_of_adults
        The total number of adult guests per booking. Defaults to ‘1’. GDS
        Providers: 1G, 1V, 1P.
    rate_rule_detail
        'None' returns hotel property descriptive information-supported for
        1p,1g/1v. 'Complete' returns the complete hotel and room rate
        information-supported for 1p,1g/1v, 'RatePlansOnly' returns hotel
        rate information only - supported for 1p, 1g/1v.
    number_of_rooms
        The number of rooms per booking. Defaults to ‘1’. GDS Providers 1G,
        1V, 1P.
    key
    preferred_currency
        Alternate currency
    total_occupants
        Number of guests for the room.  Supported Providers: 1P
    process_all_nego_rates_ind
        When false, we will process the request with all the provided
        negotiated rates in a single request. The request will fail when the
        number of negotiated rates have exceeded for that hotel chain. When
        true, this allows to process a request for all provided negotiated
        rates that may exceed the hotel chain limit. Supported for 1P only.
    max_wait
        Maximum wait time in milliseconds for hotel detail results.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    permitted_providers: None | PermittedProviders1 = field(
        default=None,
        metadata={
            "name": "PermittedProviders",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 4,
        }
    )
    corporate_discount_id: list[CorporateDiscountId1] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    hotel_stay: None | HotelStay = field(
        default=None,
        metadata={
            "name": "HotelStay",
            "type": "Element",
            "required": True,
        }
    )
    number_of_children: None | NumberOfChildren = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Element",
        }
    )
    hotel_bedding: list[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "max_occurs": 4,
        }
    )
    rate_category: list[int] = field(
        default_factory=list,
        metadata={
            "name": "RateCategory",
            "type": "Element",
            "max_occurs": 8,
        }
    )
    booking_guest_information: None | BookingGuestInformation = field(
        default=None,
        metadata={
            "name": "BookingGuestInformation",
            "type": "Element",
        }
    )
    number_of_adults: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Attribute",
        }
    )
    rate_rule_detail: TypeRateRuleDetail = field(
        default=TypeRateRuleDetail.NONE,
        metadata={
            "name": "RateRuleDetail",
            "type": "Attribute",
        }
    )
    number_of_rooms: int = field(
        default=1,
        metadata={
            "name": "NumberOfRooms",
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
    preferred_currency: None | str = field(
        default=None,
        metadata={
            "name": "PreferredCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )
    total_occupants: None | int = field(
        default=None,
        metadata={
            "name": "TotalOccupants",
            "type": "Attribute",
        }
    )
    process_all_nego_rates_ind: bool = field(
        default=False,
        metadata={
            "name": "ProcessAllNegoRatesInd",
            "type": "Attribute",
        }
    )
    max_wait: None | int = field(
        default=None,
        metadata={
            "name": "MaxWait",
            "type": "Attribute",
        }
    )
