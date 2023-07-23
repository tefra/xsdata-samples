from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_info_1 import AgencyInfo1
from travelport.models.air_pricing_info import AirPricingInfo
from travelport.models.audit_data import AuditData
from travelport.models.baggage_allowances import BaggageAllowances
from travelport.models.booking_traveler_1 import BookingTraveler1
from travelport.models.commission_1 import Commission1
from travelport.models.credit_card_auth_1 import CreditCardAuth1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.payment_1 import Payment1
from travelport.models.restriction_1 import Restriction1
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.ticket import Ticket
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.waiver_code import WaiverCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Etr:
    """
    Result of ticketing request.

    Parameters
    ----------
    air_reservation_locator_code
    agency_info
    booking_traveler
    form_of_payment
    payment
    credit_card_auth
        This is a container to display detail information of credit card
        auth. Providers supported: Worldspan.
    supplier_locator
    fare_calc
    ticket
    commission
    air_pricing_info
    audit_data
    restriction
    waiver_code
    baggage_allowances
        Baggage Allowance Info after Ticketing
    key
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
    refundable
    exchangeable
    tour_code
    issued_date
        Ticket issue date.
    bulk_ticket
        Whether the ticket was issued as bulk.
    provider_code
        Contains the Provider Code of the provider that houses this ETR.
    provider_locator_code
        Contains the Locator Code of the Provider Reservation that houses
        this ETR.
    iatanumber
        Contains the IATA Number of the agent initiating the request.
    pseudo_city_code
        Contain Pseudo City, city/office number, branch ID, etc.
    country_code
        Contains Ticketed PCC’s Country code.
    plating_carrier
        Contains the Plating Carrier of this ETR.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """
    class Meta:
        name = "ETR"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        }
    )
    agency_info: None | AgencyInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    booking_traveler: None | BookingTraveler1 = field(
        default=None,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )
    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    payment: list[Payment1] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    credit_card_auth: list[CreditCardAuth1] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    fare_calc: None | str = field(
        default=None,
        metadata={
            "name": "FareCalc",
            "type": "Element",
            "required": True,
        }
    )
    ticket: list[Ticket] = field(
        default_factory=list,
        metadata={
            "name": "Ticket",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    commission: list[Commission1] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    air_pricing_info: None | AirPricingInfo = field(
        default=None,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
        }
    )
    audit_data: None | AuditData = field(
        default=None,
        metadata={
            "name": "AuditData",
            "type": "Element",
        }
    )
    restriction: list[Restriction1] = field(
        default_factory=list,
        metadata={
            "name": "Restriction",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    waiver_code: None | WaiverCode = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Element",
        }
    )
    baggage_allowances: None | BaggageAllowances = field(
        default=None,
        metadata={
            "name": "BaggageAllowances",
            "type": "Element",
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
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
    refundable: None | bool = field(
        default=None,
        metadata={
            "name": "Refundable",
            "type": "Attribute",
        }
    )
    exchangeable: None | bool = field(
        default=None,
        metadata={
            "name": "Exchangeable",
            "type": "Attribute",
        }
    )
    tour_code: None | str = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    issued_date: None | str = field(
        default=None,
        metadata={
            "name": "IssuedDate",
            "type": "Attribute",
            "required": True,
        }
    )
    bulk_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "BulkTicket",
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
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    iatanumber: None | str = field(
        default=None,
        metadata={
            "name": "IATANumber",
            "type": "Attribute",
            "max_length": 8,
        }
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    country_code: None | str = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    plating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
