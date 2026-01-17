from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.accepted_payment import AcceptedPayment
from travelport.models.cancel_info import CancelInfo
from travelport.models.commission_2 import Commission2
from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.guarantee_info import GuaranteeInfo
from travelport.models.hotel_rate_by_date import HotelRateByDate
from travelport.models.rate_match_indicator import RateMatchIndicator
from travelport.models.room_view import RoomView
from travelport.models.tax_details import TaxDetails
from travelport.models.type_hotel_rate_description import (
    TypeHotelRateDescription,
)
from travelport.models.type_policy_codes_list_1 import TypePolicyCodesList1
from travelport.models.type_trinary import TypeTrinary

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelRateDetail:
    """
    Returns hotel rate details during the stay if rates are available for
    requested property.

    Parameters
    ----------
    policy_codes_list
        A list of codes that indicate why an item was determined to be ‘out
        of policy’.
    room_rate_description
    hotel_rate_by_date
    corporate_discount_id
        Corporate Discount IDs and Negotiate rate codes associated with this
        rate
    accepted_payment
        Form of payment accepted by the hotel supplier (chain or property).
        For credit cards, the two-character code for the credit card type is
        used.
    commission
        Commission associated with the Rate Plan, as a percentage or flat
        amount.
    rate_match_indicator
        Returns "Match" Indicators for certain request parameters for Hotel
        Rate returned in response.
    tax_details
    cancel_info
    guarantee_info
        Guarantee, deposit, and prepayment information
    supplemental_rate_info
        Supplemental rate information provided by the aggregator.
    room_capacity
        The maximum number of guests for a room or for each room in a
        package.
    extra_charges
        Additional charges applied to the hotel rate.
    inclusions
        Additional items included in the hotel rate plan.
    rate_plan_type
    base
        This attribute is used to describe the Hotel Supplier Base Rate
    tax
        This attribute used to describe Tax associated with the room
    total
        This attribute used to describe Hotel Supplier Total Rate
    surcharge
        This attribute used to describe Surcharge associated with the room
    approximate_base
        Hotel base rate expressed in another currency
    approximate_tax
        Taxes expressed in another currency
    approximate_total
        Hotel total rate expressed in another currency.
    approximate_surcharge
        Surcharge associated with the room expressed in another currency.
    rate_guaranteed
    approximate_rate_guaranteed
        If true, approximate rate is guaranteed by vendor.  Supported
        Providers: 1G,1V
    rate_category
        An enumerated type that allows the query to specify a rate category
        type, and provides major categories for comparison across brands.
        Refer to OpenTravel Code List Rate Plan Type (RPT). Encode/decode
        data in Util ReferenceDataRetrieveReq TypeCode=“HotelRateCategory".
    key
    rate_supplier
        Indicates the source of the rate.
    bookable_quantity
        The number of rooms which can be booked on the rate returned in
        HotelRateDetails.  When the aggregator responds ‘IsPackage’= true
        (pricing for all rooms together), the BookableQuantity value will be
        ‘1’.
    rate_offer_id
        Offer Identifier. Maybe required for hotels provided by aggregators.
    in_policy
        This attribute will be used to indicate if a fare or rate has been
        determined to be ‘in policy’ based on the associated policy
        settings.
    rate_change_indicator
        Determines if the rate changes during the length of stay. Enumerated
        values are true, false, and unknown.
    extra_fees_included
        When true, total amounts includes additional fees or charges."
        Enumerated values are true, false, and unknown
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    policy_codes_list: None | TypePolicyCodesList1 = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
        },
    )
    room_rate_description: list[TypeHotelRateDescription] = field(
        default_factory=list,
        metadata={
            "name": "RoomRateDescription",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_rate_by_date: list[HotelRateByDate] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateByDate",
            "type": "Element",
            "max_occurs": 999,
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
    accepted_payment: list[AcceptedPayment] = field(
        default_factory=list,
        metadata={
            "name": "AcceptedPayment",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    commission: None | Commission2 = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        },
    )
    rate_match_indicator: list[RateMatchIndicator] = field(
        default_factory=list,
        metadata={
            "name": "RateMatchIndicator",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tax_details: None | TaxDetails = field(
        default=None,
        metadata={
            "name": "TaxDetails",
            "type": "Element",
        },
    )
    cancel_info: None | CancelInfo = field(
        default=None,
        metadata={
            "name": "CancelInfo",
            "type": "Element",
        },
    )
    guarantee_info: None | GuaranteeInfo = field(
        default=None,
        metadata={
            "name": "GuaranteeInfo",
            "type": "Element",
        },
    )
    supplemental_rate_info: None | str = field(
        default=None,
        metadata={
            "name": "SupplementalRateInfo",
            "type": "Element",
        },
    )
    room_capacity: None | HotelRateDetail.RoomCapacity = field(
        default=None,
        metadata={
            "name": "RoomCapacity",
            "type": "Element",
        },
    )
    extra_charges: None | HotelRateDetail.ExtraCharges = field(
        default=None,
        metadata={
            "name": "ExtraCharges",
            "type": "Element",
        },
    )
    inclusions: None | HotelRateDetail.Inclusions = field(
        default=None,
        metadata={
            "name": "Inclusions",
            "type": "Element",
        },
    )
    rate_plan_type: None | str = field(
        default=None,
        metadata={
            "name": "RatePlanType",
            "type": "Attribute",
            "required": True,
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "name": "Base",
            "type": "Attribute",
        },
    )
    tax: None | str = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Attribute",
        },
    )
    total: None | str = field(
        default=None,
        metadata={
            "name": "Total",
            "type": "Attribute",
        },
    )
    surcharge: None | str = field(
        default=None,
        metadata={
            "name": "Surcharge",
            "type": "Attribute",
        },
    )
    approximate_base: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBase",
            "type": "Attribute",
        },
    )
    approximate_tax: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTax",
            "type": "Attribute",
        },
    )
    approximate_total: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotal",
            "type": "Attribute",
        },
    )
    approximate_surcharge: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateSurcharge",
            "type": "Attribute",
        },
    )
    rate_guaranteed: None | bool = field(
        default=None,
        metadata={
            "name": "RateGuaranteed",
            "type": "Attribute",
        },
    )
    approximate_rate_guaranteed: None | bool = field(
        default=None,
        metadata={
            "name": "ApproximateRateGuaranteed",
            "type": "Attribute",
        },
    )
    rate_category: None | int = field(
        default=None,
        metadata={
            "name": "RateCategory",
            "type": "Attribute",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    rate_supplier: None | str = field(
        default=None,
        metadata={
            "name": "RateSupplier",
            "type": "Attribute",
            "max_length": 64,
        },
    )
    bookable_quantity: None | int = field(
        default=None,
        metadata={
            "name": "BookableQuantity",
            "type": "Attribute",
        },
    )
    rate_offer_id: None | str = field(
        default=None,
        metadata={
            "name": "RateOfferId",
            "type": "Attribute",
        },
    )
    in_policy: None | bool = field(
        default=None,
        metadata={
            "name": "InPolicy",
            "type": "Attribute",
        },
    )
    rate_change_indicator: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "RateChangeIndicator",
            "type": "Attribute",
        },
    )
    extra_fees_included: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "ExtraFeesIncluded",
            "type": "Attribute",
        },
    )

    @dataclass
    class RoomCapacity:
        """
        Parameters
        ----------
        capacity
            The maximum number of guests per room.
        is_package
            If true, the rooms are offered as a package by the aggregator.
        """

        capacity: list[int] = field(
            default_factory=list,
            metadata={
                "name": "Capacity",
                "type": "Element",
                "max_occurs": 99,
            },
        )
        is_package: None | bool = field(
            default=None,
            metadata={
                "name": "IsPackage",
                "type": "Attribute",
            },
        )

    @dataclass
    class ExtraCharges:
        """
        Parameters
        ----------
        extra_adult_amount
            Additional charge for an extra guest.
        extra_child_amount
            dditional charge for an extra child guest.
        crib_amount
            Additional charge for a crib.
        adult_rollaway_charge
            Additional charge for an extra rollaway bed provided for an
            adult guest.
        child_rollaway_charge
            Additional charge for an extra rollaway bed provided for a child
            guest.
        """

        extra_adult_amount: None | str = field(
            default=None,
            metadata={
                "name": "ExtraAdultAmount",
                "type": "Attribute",
            },
        )
        extra_child_amount: None | str = field(
            default=None,
            metadata={
                "name": "ExtraChildAmount",
                "type": "Attribute",
            },
        )
        crib_amount: None | str = field(
            default=None,
            metadata={
                "name": "CribAmount",
                "type": "Attribute",
            },
        )
        adult_rollaway_charge: None | str = field(
            default=None,
            metadata={
                "name": "AdultRollawayCharge",
                "type": "Attribute",
            },
        )
        child_rollaway_charge: None | str = field(
            default=None,
            metadata={
                "name": "ChildRollawayCharge",
                "type": "Attribute",
            },
        )

    @dataclass
    class Inclusions:
        """
        Parameters
        ----------
        bed_types
            Bed types in the rate plan.
        meal_plans
            Meal options available for the rate plan.
        room_view
            The view from the hotel room.
        smoking_room_indicator
            Indicates if the room is designated as nonsmoking or smoking.
            true = Smoking false = NonSmoking unknown = Information is not
            returned by the hotel supplier (chain or property).
        """

        bed_types: list[HotelRateDetail.Inclusions.BedTypes] = field(
            default_factory=list,
            metadata={
                "name": "BedTypes",
                "type": "Element",
                "max_occurs": 99,
            },
        )
        meal_plans: None | HotelRateDetail.Inclusions.MealPlans = field(
            default=None,
            metadata={
                "name": "MealPlans",
                "type": "Element",
            },
        )
        room_view: None | RoomView = field(
            default=None,
            metadata={
                "name": "RoomView",
                "type": "Element",
            },
        )
        smoking_room_indicator: None | TypeTrinary = field(
            default=None,
            metadata={
                "name": "SmokingRoomIndicator",
                "type": "Attribute",
            },
        )

        @dataclass
        class BedTypes:
            """
            Parameters
            ----------
            code
                Bed Type Code. Uses Open Travel Code List Room Amenity Type
                (RMA). Encode/decode data in Util ReferenceDataRetrieveReq
                TypeCode=“HotelAmenities”.
            quantity
                Bed Quantity.
            """

            code: None | int = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                },
            )
            quantity: None | int = field(
                default=None,
                metadata={
                    "name": "Quantity",
                    "type": "Attribute",
                },
            )

        @dataclass
        class MealPlans:
            """
            Parameters
            ----------
            meal_plan
                Meal plan.
            breakfast
                Indicates whether a daily breakfast is included in the meal
                plan. true = Breakfast is included false = Breakfast is not
                included unknown = Information is not returned by the hotel
                supplier (chain or property).
            lunch
                Indicates whether a daily lunch is included in the meal
                plan. true = Lunch is included false = Lunch is not included
                unknown = Information is not returned by the hotel supplier
                (chain or property).
            dinner
                Indicates whether a daily dinner is included in the meal
                plan. true = Dinner is included false = Dinner is not
                included unknown = Information is not returned by the hotel
                supplier (chain or property).
            """

            meal_plan: list[HotelRateDetail.Inclusions.MealPlans.MealPlan] = (
                field(
                    default_factory=list,
                    metadata={
                        "name": "MealPlan",
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )
            )
            breakfast: None | TypeTrinary = field(
                default=None,
                metadata={
                    "name": "Breakfast",
                    "type": "Attribute",
                },
            )
            lunch: None | TypeTrinary = field(
                default=None,
                metadata={
                    "name": "Lunch",
                    "type": "Attribute",
                },
            )
            dinner: None | TypeTrinary = field(
                default=None,
                metadata={
                    "name": "Dinner",
                    "type": "Attribute",
                },
            )

            @dataclass
            class MealPlan:
                """
                Parameters
                ----------
                code
                    Meal plan code. Uses Open Travel Code List Meal Plan
                    Type (MPT). Encode/decode data in Util
                    ReferenceDataRetrieveReq TypeCode=“HotelMealPlans”.
                """

                code: None | int = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                    },
                )
