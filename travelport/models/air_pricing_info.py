from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.action_details import ActionDetails
from travelport.models.adjustment import Adjustment
from travelport.models.air_pricing_modifiers import AirPricingModifiers
from travelport.models.air_segment_pricing_modifiers import (
    AirSegmentPricingModifiers,
)
from travelport.models.baggage_allowances import BaggageAllowances
from travelport.models.booking_info import BookingInfo
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.commission_1 import Commission1
from travelport.models.fare_calc import FareCalc
from travelport.models.fare_info import FareInfo
from travelport.models.fare_info_ref import FareInfoRef
from travelport.models.fare_rules_filter import FareRulesFilter
from travelport.models.fare_status import FareStatus
from travelport.models.fee_info import FeeInfo
from travelport.models.flight_options_list import FlightOptionsList
from travelport.models.passenger_type import PassengerType
from travelport.models.payment_ref_2 import PaymentRef2
from travelport.models.policy_codes_list import PolicyCodesList
from travelport.models.price_change_type import PriceChangeType
from travelport.models.tax_info import TaxInfo
from travelport.models.ticketing_modifiers_ref import TicketingModifiersRef
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_eticketability import TypeEticketability
from travelport.models.type_fare_penalty import TypeFarePenalty
from travelport.models.type_most_restrictive_penalties import (
    TypeMostRestrictivePenalties,
)
from travelport.models.type_pricing_method import TypePricingMethod
from travelport.models.waiver_code import WaiverCode
from travelport.models.yield_mod import Yield

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPricingInfo:
    """Per traveler type pricing breakdown.

    This will reflect the pricing for all travelers of the specified
    type.

    Parameters
    ----------
    fare_info
    fare_status
    fare_info_ref
    booking_info
    tax_info
    fare_calc
    passenger_type
    booking_traveler_ref
    waiver_code
    payment_ref
        The reference to the Payment if Air Pricing is charged
    change_penalty
        The penalty (if any) to change the itinerary
    cancel_penalty
        The penalty (if any) to cancel the fare
    no_show_penalty
        The NoShow penalty (if any)
    most_restrictive_penalties
        Contain CAT16 Most Restrictive Penalties.
    fee_info
    adjustment
    yield_value
    air_pricing_modifiers
    ticketing_modifiers_ref
    air_segment_pricing_modifiers
    flight_options_list
    baggage_allowances
    fare_rules_filter
    policy_codes_list
        A list of codes that indicate why an item was determined to be ‘out
        of policy’
    price_change
        Indicates a price change is found in Fare Control Manager
    action_details
    commission
        Allows an agency to update the commission to a new or different
        commission rate which will be applied at time of ticketing. The
        commission Modifier allows the user specify how the commission
        change is to applied
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    key
    command_key
        The command identifier used when this is in response to an
        AirPricingCommand. Not used in any request processing.
    total_price
        The total price for this entity including base price and all taxes.
    base_price
        Represents the base price for this entity. This does not include any
        taxes or surcharges.
    approximate_total_price
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    approximate_base_price
        The Converted base price in Default Currency for this entity. This
        does not include any taxes or surcharges.
    equivalent_base_price
        Represents the base price in the related currency for this entity.
        This does not include any taxes or surcharges.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated TaxInfo array for a breakdown of the
        individual taxes.
    fees
        The aggregated amount of all the fees that are associated with this
        entity. See the associated FeeInfo array for a breakdown of the
        individual fees.
    services
        The total cost for all optional services.
    approximate_taxes
        The Converted tax amount in Default Currency.
    approximate_fees
        The Converted fee amount in Default Currency.
    provider_code
    supplier_code
    amount_type
        This field displays type of payment amount when it is non-monetary.
        Presently available/supported value is "Flight Pass Credits".
    includes_vat
        Indicates whether the Base Price includes VAT.
    exchange_amount
        The amount to pay to cover the exchange of the fare (includes
        penalties).
    forfeit_amount
        The amount forfeited when the fare is exchanged.
    refundable
        Indicates whether the fare is refundable
    exchangeable
        Indicates whether the fare is exchangeable
    latest_ticketing_time
        The latest date/time at which this pricing information is valid
    pricing_method
    checksum
        A security value used to guarantee that the pricing data sent in
        matches the pricing data previously returned
    eticketability
        The E-Ticketability of this AirPricing
    plating_carrier
        The Plating Carrier for this journey
    provider_reservation_info_ref
        Provider reservation reference key.
    air_pricing_info_group
        This attribute is added to support multiple store fare in Host. All
        AirPricingInfo with same group number will be stored together.
    total_net_price
        The total price of a negotiated fare.
    ticketed
        Indicates if the associated stored fare is ticketed or not.
    pricing_type
        Indicates the Pricing Type used. The possible values are
        TicketRecord, StoredFare, PricingInstruction.
    true_last_date_to_ticket
        This date indicates the true last date/time to ticket for the fare.
        This date comes from the filed fare . There is no guarantee the fare
        will still be available on that date or that the fare amount may
        change. It is merely the last date to purchase a ticket based on the
        carriers fare rules at the time the itinerary was quoted and stored
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    in_policy
        This attribute will be used to indicate if a fare or rate has been
        determined to be ‘in policy’ based on the associated policy
        settings.
    preferred_option
        This attribute is used to indicate if the vendors responsible for
        the fare or rate being returned have been determined to be
        ‘preferred’ based on the associated policy settings.
    fare_calculation_ind
        Fare calculation that was used to price the itinerary.
    cat35_indicator
        A true value indicates that the fare has a Cat35 rule. A false valud
        indicates that the fare does not have a Cat35 rule
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_info: list[FareInfo] = field(
        default_factory=list,
        metadata={
            "name": "FareInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_status: None | FareStatus = field(
        default=None,
        metadata={
            "name": "FareStatus",
            "type": "Element",
        },
    )
    fare_info_ref: list[FareInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "FareInfoRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    booking_info: list[BookingInfo] = field(
        default_factory=list,
        metadata={
            "name": "BookingInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_calc: None | FareCalc = field(
        default=None,
        metadata={
            "name": "FareCalc",
            "type": "Element",
        },
    )
    passenger_type: list[PassengerType] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    waiver_code: None | WaiverCode = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        },
    )
    payment_ref: list[PaymentRef2] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    change_penalty: list[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "name": "ChangePenalty",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    cancel_penalty: list[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "name": "CancelPenalty",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    no_show_penalty: list[TypeFarePenalty] = field(
        default_factory=list,
        metadata={
            "name": "NoShowPenalty",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    most_restrictive_penalties: None | TypeMostRestrictivePenalties = field(
        default=None,
        metadata={
            "name": "MostRestrictivePenalties",
            "type": "Element",
        },
    )
    fee_info: list[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    adjustment: list[Adjustment] = field(
        default_factory=list,
        metadata={
            "name": "Adjustment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    yield_value: list[Yield] = field(
        default_factory=list,
        metadata={
            "name": "Yield",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_pricing_modifiers: None | AirPricingModifiers = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
        },
    )
    ticketing_modifiers_ref: list[TicketingModifiersRef] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiersRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_segment_pricing_modifiers: list[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    flight_options_list: None | FlightOptionsList = field(
        default=None,
        metadata={
            "name": "FlightOptionsList",
            "type": "Element",
        },
    )
    baggage_allowances: None | BaggageAllowances = field(
        default=None,
        metadata={
            "name": "BaggageAllowances",
            "type": "Element",
        },
    )
    fare_rules_filter: None | FareRulesFilter = field(
        default=None,
        metadata={
            "name": "FareRulesFilter",
            "type": "Element",
        },
    )
    policy_codes_list: None | PolicyCodesList = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
        },
    )
    price_change: list[PriceChangeType] = field(
        default_factory=list,
        metadata={
            "name": "PriceChange",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    action_details: None | ActionDetails = field(
        default=None,
        metadata={
            "name": "ActionDetails",
            "type": "Element",
        },
    )
    commission: list[Commission1] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    command_key: None | str = field(
        default=None,
        metadata={
            "name": "CommandKey",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        },
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        },
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        },
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        },
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        },
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        },
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        },
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        },
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        },
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    amount_type: None | str = field(
        default=None,
        metadata={
            "name": "AmountType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    includes_vat: None | bool = field(
        default=None,
        metadata={
            "name": "IncludesVAT",
            "type": "Attribute",
        },
    )
    exchange_amount: None | str = field(
        default=None,
        metadata={
            "name": "ExchangeAmount",
            "type": "Attribute",
        },
    )
    forfeit_amount: None | str = field(
        default=None,
        metadata={
            "name": "ForfeitAmount",
            "type": "Attribute",
        },
    )
    refundable: None | bool = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
        },
    )
    exchangeable: None | bool = field(
        default=None,
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
        },
    )
    latest_ticketing_time: None | str = field(
        default=None,
        metadata={
            "name": "LatestTicketingTime",
            "type": "Attribute",
        },
    )
    pricing_method: None | TypePricingMethod = field(
        default=None,
        metadata={
            "name": "PricingMethod",
            "type": "Attribute",
            "required": True,
        },
    )
    checksum: None | str = field(
        default=None,
        metadata={
            "name": "Checksum",
            "type": "Attribute",
        },
    )
    eticketability: None | TypeEticketability = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
        },
    )
    plating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    air_pricing_info_group: None | int = field(
        default=None,
        metadata={
            "name": "AirPricingInfoGroup",
            "type": "Attribute",
        },
    )
    total_net_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalNetPrice",
            "type": "Attribute",
        },
    )
    ticketed: None | bool = field(
        default=None,
        metadata={
            "name": "Ticketed",
            "type": "Attribute",
        },
    )
    pricing_type: None | str = field(
        default=None,
        metadata={
            "name": "PricingType",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    true_last_date_to_ticket: None | str = field(
        default=None,
        metadata={
            "name": "TrueLastDateToTicket",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
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
    preferred_option: None | bool = field(
        default=None,
        metadata={
            "name": "PreferredOption",
            "type": "Attribute",
        },
    )
    fare_calculation_ind: None | str = field(
        default=None,
        metadata={
            "name": "FareCalculationInd",
            "type": "Attribute",
            "length": 1,
        },
    )
    cat35_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "Cat35Indicator",
            "type": "Attribute",
        },
    )
