from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.balance import Balance
from travelport.models.charges import Charges
from travelport.models.commission_3 import Commission3
from travelport.models.cruise_booking_traveler_ref import CruiseBookingTravelerRef
from travelport.models.cruise_fees import CruiseFees
from travelport.models.deposit import Deposit
from travelport.models.discount import Discount
from travelport.models.fare import Fare

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class CruisePricingInfo:
    """Cruise pricing Information.

    Contains all related pricing data for travelers.

    Parameters
    ----------
    fare
    charges
    discount
    deposit
    balance
    commission
    cruise_fees
    cruise_booking_traveler_ref
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
    net_fare
        Net Fare amount (Base price plus miscellaneouscharges less
        discounts)
    received_amount
        Amount of money Recieved
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    fare: None | Fare = field(
        default=None,
        metadata={
            "name": "Fare",
            "type": "Element",
        }
    )
    charges: None | Charges = field(
        default=None,
        metadata={
            "name": "Charges",
            "type": "Element",
        }
    )
    discount: list[Discount] = field(
        default_factory=list,
        metadata={
            "name": "Discount",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    deposit: list[Deposit] = field(
        default_factory=list,
        metadata={
            "name": "Deposit",
            "type": "Element",
            "max_occurs": 2,
        }
    )
    balance: None | Balance = field(
        default=None,
        metadata={
            "name": "Balance",
            "type": "Element",
        }
    )
    commission: None | Commission3 = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        }
    )
    cruise_fees: None | CruiseFees = field(
        default=None,
        metadata={
            "name": "CruiseFees",
            "type": "Element",
        }
    )
    cruise_booking_traveler_ref: list[CruiseBookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "CruiseBookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    net_fare: None | str = field(
        default=None,
        metadata={
            "name": "NetFare",
            "type": "Attribute",
        }
    )
    received_amount: None | str = field(
        default=None,
        metadata={
            "name": "ReceivedAmount",
            "type": "Attribute",
        }
    )
