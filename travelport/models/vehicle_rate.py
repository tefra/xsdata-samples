from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.priced_equip import PricedEquip
from travelport.models.rate_inclusions import RateInclusions
from travelport.models.supplier_rate import SupplierRate
from travelport.models.type_distance import TypeDistance
from travelport.models.type_rate_availability import TypeRateAvailability
from travelport.models.type_rate_category import TypeRateCategory
from travelport.models.type_rate_guarantee import TypeRateGuarantee
from travelport.models.type_rate_host_indicator import TypeRateHostIndicator
from travelport.models.type_rate_info import TypeRateInfo
from travelport.models.type_rate_time_period import TypeRateTimePeriod
from travelport.models.type_rate_variance import TypeRateVariance
from travelport.models.type_trinary import TypeTrinary
from travelport.models.type_vehicle_charge import TypeVehicleCharge
from travelport.models.type_vehicle_rate_description import (
    TypeVehicleRateDescription,
)
from travelport.models.type_vehicle_rates import TypeVehicleRates
from travelport.models.vehicle_rate_required_payment import (
    VehicleRateRequiredPayment,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleRate:
    """
    Rate summary.

    Parameters
    ----------
    supplier_rate
    rate_variance
        Used on VehicleCreateReservationReq ONLY. @MandatoryRateMatch
        ='true' is required for this element to be applied. 1P.
    approximate_rate
        Monetary amounts expressed in another currency
    vehicle_charge
        Charges associated with the vehicle rental.
    vehicle_rate_description
    rate_host_indicator
    hourly_late_charge
    daily_late_charge
    priced_equip
    rate_inclusions
    weekly_late_charge
        Extra Week Charges information. Supported providers:1P only
    print_text
        Informational text provided by the supplier that may be related to
        the reservation. This is applicable in response messages only, 1p
        only.
    rate_period
        The period for the rate (daily, weekly, etc)
    number_of_periods
        Define how many periods (e.g. number of days or weeks)
    unlimited_mileage
        True if unlimited miles for rate
    mileage_allowance
        Only set if UnlimitedMileage is false. Number of miles allowed for
        rate
    units
        Describes distance units for MileageAllowance or ExtraMileageCharge
    rate_source
        The rate source indicator for GWS
    rate_availability
        Rate is available to sell, Need to Call or Closed
    required_charges
    rate_code
        Rate Code of the vehicle. Supported Providers 1P,1G,1V.
    requested_rate_code_applied
        The requested Rate Code applied to the Rate. Valid values: "true",
        "false", "unknown". Supported Providers 1P.
    rate_category
        The category of this rate (Best, etc)
    discount_number
        Corporate Discount number used to request a specified discount.
        Supported Providers Requests: 1P,1G,1V, Responses only 1P.
    discount_number_applied
        Discount Number has been applied to the Rate. Valid values: "true",
        "false", "unknown". Supported Providers 1P.
    vendor_code
    rate_guaranteed
        Guarantee indicator for vehicle rate.
    rate_code_period
        RateCodePeriod
    promotional_code
        Specific coupon or promotion code. Providers 1P,1V,1G.
    promotional_code_applied
        Promotional/Coupon Number has been applied to the Rate. Valid
        values: "true", "false", "unknown". Supported Providers 1P.
    tour_code
        Tour Number for the Vehicle Booking
    tour_code_applied
        Tour Code Number has been applied to the Rate. Valid values: "true",
        "false", "unknown". Supported Providers 1P.
    rate_guarantee_type
        To identify whether rate is already guaranteed or rate quoted or
        agent entered
    required_payment
        Returns Payment information required by vendor at the time og
        booking.
    drop_off_charges_included
        If true: Drop off charges are included. If false, not included. If
        not specified, additional drop off charges MAY apply (but this has
        not been confirmed by vendor)
    corporate_rate
        If "true" a Corporate Discount has been applied to the rate.
        Applicable to 1P
    advanced_booking
        Indicates the number of Hours or Days a rate must be booked in
        advance. Values are for Days = number followed by “D” e.g., "002D"
        and Hours = number followed by “H” e.g., 002H” 1P/1G/1V only.
    rental_restriction
        RentalRestriction attribute value is true if vehicle rate has rental
        restrictions. Rental restrictions can be obtained from the Vehicle
        Rules. 1P only.
    flight_restriction
        Flight restriction indicator is true if flight information is
        required at booking. 1P/1G/1V only.
    card_number
        Vehicle Loyalty Card Number. Supported Provider 1P.
    card_number_applied
        Loyalty Card Number has been applied to the Rate. Values: "true",
        "false", "unknown". Supported Providers 1P.
    rate_qualifier_ind
        Indicates whether rates comply with CD, ID, or Drop Off requested. 1
        is fully qualified, 2 is partly qualified, and 3 is other rates. 1G,
        1V only.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    supplier_rate: None | SupplierRate = field(
        default=None,
        metadata={
            "name": "SupplierRate",
            "type": "Element",
        },
    )
    rate_variance: None | TypeRateVariance = field(
        default=None,
        metadata={
            "name": "RateVariance",
            "type": "Element",
        },
    )
    approximate_rate: None | TypeVehicleRates = field(
        default=None,
        metadata={
            "name": "ApproximateRate",
            "type": "Element",
        },
    )
    vehicle_charge: list[TypeVehicleCharge] = field(
        default_factory=list,
        metadata={
            "name": "VehicleCharge",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_rate_description: list[TypeVehicleRateDescription] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRateDescription",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    rate_host_indicator: None | TypeRateHostIndicator = field(
        default=None,
        metadata={
            "name": "RateHostIndicator",
            "type": "Element",
        },
    )
    hourly_late_charge: None | TypeRateInfo = field(
        default=None,
        metadata={
            "name": "HourlyLateCharge",
            "type": "Element",
        },
    )
    daily_late_charge: None | TypeRateInfo = field(
        default=None,
        metadata={
            "name": "DailyLateCharge",
            "type": "Element",
        },
    )
    priced_equip: list[PricedEquip] = field(
        default_factory=list,
        metadata={
            "name": "PricedEquip",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rate_inclusions: None | RateInclusions = field(
        default=None,
        metadata={
            "name": "RateInclusions",
            "type": "Element",
        },
    )
    weekly_late_charge: None | TypeRateInfo = field(
        default=None,
        metadata={
            "name": "WeeklyLateCharge",
            "type": "Element",
        },
    )
    print_text: None | str = field(
        default=None,
        metadata={
            "name": "PrintText",
            "type": "Element",
        },
    )
    rate_period: None | TypeRateTimePeriod = field(
        default=None,
        metadata={
            "name": "RatePeriod",
            "type": "Attribute",
        },
    )
    number_of_periods: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfPeriods",
            "type": "Attribute",
        },
    )
    unlimited_mileage: None | bool = field(
        default=None,
        metadata={
            "name": "UnlimitedMileage",
            "type": "Attribute",
        },
    )
    mileage_allowance: None | int = field(
        default=None,
        metadata={
            "name": "MileageAllowance",
            "type": "Attribute",
        },
    )
    units: None | TypeDistance = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Attribute",
        },
    )
    rate_source: None | str = field(
        default=None,
        metadata={
            "name": "RateSource",
            "type": "Attribute",
        },
    )
    rate_availability: None | TypeRateAvailability = field(
        default=None,
        metadata={
            "name": "RateAvailability",
            "type": "Attribute",
        },
    )
    required_charges: None | str = field(
        default=None,
        metadata={
            "name": "RequiredCharges",
            "type": "Attribute",
        },
    )
    rate_code: None | str = field(
        default=None,
        metadata={
            "name": "RateCode",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    requested_rate_code_applied: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "RequestedRateCodeApplied",
            "type": "Attribute",
        },
    )
    rate_category: None | TypeRateCategory = field(
        default=None,
        metadata={
            "name": "RateCategory",
            "type": "Attribute",
        },
    )
    discount_number: None | str = field(
        default=None,
        metadata={
            "name": "DiscountNumber",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    discount_number_applied: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "DiscountNumberApplied",
            "type": "Attribute",
        },
    )
    vendor_code: None | str = field(
        default=None,
        metadata={
            "name": "VendorCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    rate_guaranteed: bool = field(
        default=False,
        metadata={
            "name": "RateGuaranteed",
            "type": "Attribute",
        },
    )
    rate_code_period: None | str = field(
        default=None,
        metadata={
            "name": "RateCodePeriod",
            "type": "Attribute",
        },
    )
    promotional_code: None | str = field(
        default=None,
        metadata={
            "name": "PromotionalCode",
            "type": "Attribute",
        },
    )
    promotional_code_applied: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "PromotionalCodeApplied",
            "type": "Attribute",
        },
    )
    tour_code: None | str = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
        },
    )
    tour_code_applied: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "TourCodeApplied",
            "type": "Attribute",
        },
    )
    rate_guarantee_type: None | TypeRateGuarantee = field(
        default=None,
        metadata={
            "name": "RateGuaranteeType",
            "type": "Attribute",
        },
    )
    required_payment: None | VehicleRateRequiredPayment = field(
        default=None,
        metadata={
            "name": "RequiredPayment",
            "type": "Attribute",
        },
    )
    drop_off_charges_included: None | bool = field(
        default=None,
        metadata={
            "name": "DropOffChargesIncluded",
            "type": "Attribute",
        },
    )
    corporate_rate: None | bool = field(
        default=None,
        metadata={
            "name": "CorporateRate",
            "type": "Attribute",
        },
    )
    advanced_booking: None | str = field(
        default=None,
        metadata={
            "name": "AdvancedBooking",
            "type": "Attribute",
        },
    )
    rental_restriction: None | bool = field(
        default=None,
        metadata={
            "name": "RentalRestriction",
            "type": "Attribute",
        },
    )
    flight_restriction: None | bool = field(
        default=None,
        metadata={
            "name": "FlightRestriction",
            "type": "Attribute",
        },
    )
    card_number: None | str = field(
        default=None,
        metadata={
            "name": "CardNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 36,
        },
    )
    card_number_applied: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "CardNumberApplied",
            "type": "Attribute",
        },
    )
    rate_qualifier_ind: None | int = field(
        default=None,
        metadata={
            "name": "RateQualifierInd",
            "type": "Attribute",
        },
    )
