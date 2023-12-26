from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.amenity import Amenity
from travelport.models.booking_guest_information import BookingGuestInformation
from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.hotel_bedding import HotelBedding
from travelport.models.hotel_chain import HotelChain
from travelport.models.hotel_rating import HotelRating
from travelport.models.loyalty_card_1 import LoyaltyCard1
from travelport.models.number_of_children import NumberOfChildren
from travelport.models.permitted_providers_1 import PermittedProviders1
from travelport.models.search_priority import SearchPriority

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelSearchModifiers:
    """
    Controls and switches for the Hotel Search request.

    Parameters
    ----------
    permitted_chains
    prohibited_chains
    permitted_providers
    loyalty_card
    hotel_name
        There can be at most one Hotel Name to be requested
    corporate_discount_id
        Search with corporate discount IDs or negotiated rate codes. 1G/1V
        allows a max of 4.  1P allows a max of 1 corporate discount ID and
        up to 30 negotiated rate codes.  Support for this function is hotel
        supplier dependent.
    rate_category
        Search for specific rate categories
    hotel_rating
    search_priority
    hotel_bedding
    amenities
        Amenity information
    number_of_children
    hotel_transportation
        OTA Transportation code. Search for specific transportation.
        Supported providers: 1G/1V.  Only CourtesyBus '7' supported by 1P.
    booking_guest_information
    number_of_adults
        The total number of adult guests per booking. Defaults to ‘1’.
        Supported Providers: 1G, 1V, 1P.
    number_of_rooms
        The number of rooms per booking. Defaults to ‘1’. Supported
        Providers 1G, 1V, 1P.
    is_relaxed
        Default is true. If false, only the results matching all the
        criteria returned.
    preferred_currency
        Requested currency for target rate.
    available_hotels_only
        Set to true to request only available hotels.  Default is false and
        all results from the provider are returned.
    max_wait
        Maximum wait time in milliseconds for hotel search results.
        Supported provider:HotelSuperShopper message.
    aggregate_results
        Indicator to identify GDS property match required or not.
    return_property_description
        Request hotel property description. Valid Values are "true" or
        "false". Default "false".
    num_of_rate_plans
        The specific number of RatePlanTypes for each property responded on
        the message, integer 1 - 999. Supported provider: HotelSuperShopper
        message only.
    return_amenities
        If hotel amenities are desired set as 'true', else default 'false'
        for no amenity support.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    permitted_chains: None | HotelSearchModifiers.PermittedChains = field(
        default=None,
        metadata={
            "name": "PermittedChains",
            "type": "Element",
        },
    )
    prohibited_chains: None | HotelSearchModifiers.ProhibitedChains = field(
        default=None,
        metadata={
            "name": "ProhibitedChains",
            "type": "Element",
        },
    )
    permitted_providers: None | PermittedProviders1 = field(
        default=None,
        metadata={
            "name": "PermittedProviders",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    loyalty_card: list[LoyaltyCard1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 4,
        },
    )
    hotel_name: None | str = field(
        default=None,
        metadata={
            "name": "HotelName",
            "type": "Element",
        },
    )
    corporate_discount_id: list[CorporateDiscountId1] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    rate_category: list[int] = field(
        default_factory=list,
        metadata={
            "name": "RateCategory",
            "type": "Element",
            "max_occurs": 8,
        },
    )
    hotel_rating: list[HotelRating] = field(
        default_factory=list,
        metadata={
            "name": "HotelRating",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    search_priority: None | SearchPriority = field(
        default=None,
        metadata={
            "name": "SearchPriority",
            "type": "Element",
        },
    )
    hotel_bedding: list[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "max_occurs": 4,
        },
    )
    amenities: None | HotelSearchModifiers.Amenities = field(
        default=None,
        metadata={
            "name": "Amenities",
            "type": "Element",
        },
    )
    number_of_children: None | NumberOfChildren = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Element",
        },
    )
    hotel_transportation: None | HotelSearchModifiers.HotelTransportation = (
        field(
            default=None,
            metadata={
                "name": "HotelTransportation",
                "type": "Element",
            },
        )
    )
    booking_guest_information: None | BookingGuestInformation = field(
        default=None,
        metadata={
            "name": "BookingGuestInformation",
            "type": "Element",
        },
    )
    number_of_adults: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Attribute",
        },
    )
    number_of_rooms: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfRooms",
            "type": "Attribute",
        },
    )
    is_relaxed: None | bool = field(
        default=None,
        metadata={
            "name": "IsRelaxed",
            "type": "Attribute",
        },
    )
    preferred_currency: None | str = field(
        default=None,
        metadata={
            "name": "PreferredCurrency",
            "type": "Attribute",
            "length": 3,
        },
    )
    available_hotels_only: None | bool = field(
        default=None,
        metadata={
            "name": "AvailableHotelsOnly",
            "type": "Attribute",
        },
    )
    max_wait: None | int = field(
        default=None,
        metadata={
            "name": "MaxWait",
            "type": "Attribute",
        },
    )
    aggregate_results: bool = field(
        default=False,
        metadata={
            "name": "AggregateResults",
            "type": "Attribute",
        },
    )
    return_property_description: bool = field(
        default=False,
        metadata={
            "name": "ReturnPropertyDescription",
            "type": "Attribute",
        },
    )
    num_of_rate_plans: None | int = field(
        default=None,
        metadata={
            "name": "NumOfRatePlans",
            "type": "Attribute",
        },
    )
    return_amenities: bool = field(
        default=False,
        metadata={
            "name": "ReturnAmenities",
            "type": "Attribute",
        },
    )

    @dataclass
    class PermittedChains:
        hotel_chain: list[HotelChain] = field(
            default_factory=list,
            metadata={
                "name": "HotelChain",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class ProhibitedChains:
        hotel_chain: list[HotelChain] = field(
            default_factory=list,
            metadata={
                "name": "HotelChain",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class Amenities:
        amenity: list[Amenity] = field(
            default_factory=list,
            metadata={
                "name": "Amenity",
                "type": "Element",
                "max_occurs": 8,
            },
        )

    @dataclass
    class HotelTransportation:
        """
        Parameters
        ----------
        type_value
            Transportation type code
        """

        type_value: None | int = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "required": True,
            },
        )
