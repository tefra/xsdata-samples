from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.air_itinerary import AirItinerary
from travelport.models.air_pricing_command import AirPricingCommand
from travelport.models.air_pricing_modifiers import AirPricingModifiers
from travelport.models.base_core_req_1 import BaseCoreReq1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.optional_services import OptionalServices
from travelport.models.pcc import Pcc
from travelport.models.search_passenger_1 import SearchPassenger1
from travelport.models.ssr_1 import Ssr1
from travelport.models.type_fare_rule_type import TypeFareRuleType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaseAirPriceReq(BaseCoreReq1):
    """
    Parameters
    ----------
    air_itinerary
        Provider: 1G,1V,1P,ACH.
    air_pricing_modifiers
        Provider: 1G,1V,1P,ACH.
    search_passenger
        Provider: 1G,1V,1P,ACH-Maxinumber of passenger increased in to 18 to
        support 9 INF passenger along with 9 ADT,CHD,INS
        passenger
    air_pricing_command
        Provider: 1G,1V,1P,ACH.
    air_reservation_locator_code
        Provider: ACH,1P
    optional_services
        Provider: ACH.
    form_of_payment
        Provider: 1G,1V,1P,ACH.
    pcc
    ssr
        Special Service Request for GST tax details. Provider: ACH
    check_obfees
        A flag to return fees for ticketing and for various forms of
        payment. The default is “TicketingOnly” and will return only
        ticketing fees.  The value “All” will return ticketing fees and the
        applicable form of payment fees for the form of payment information
        specified in the request.  “FOPOnly” will return the applicable form
        of payment fees for the form of payment information specified in the
        request. Form of payment fees are never included in the total unless
        specific card details are in the request.Provider notes:ACH -
        CheckOBFees is valid only for LowFareSearch.  The valid values are
        “All”, “TicketingOnly” and “None” and the default value is “None”.
        1P -The valid values are “All”, “None” and “TicketingOnly”.1G – All
        four values are supported.1V/RCH – CheckOBFees are not supported.”
    fare_rule_type
        Provider: 1G,1V,1P,ACH.
    supplier_code
        Specifies the supplier/ vendor for vendor specific price requests
    ticket_date
        YYYY-MM-DD Using a date in the past is a request for an historical
        fare
    check_flight_details
        To Include FlightDetails in Response set to “true” the Default value
        is “false”.
    return_mm
        If this attribute is set to “true”, Fare Control Manager processing
        will be invoked.
    nscc
        1 to 3 numeric that defines a Search Control Console filter.This
        attribute is used to override that filter.
    split_pricing
        Indicates whether the AirSegments should be priced together or
        separately. Set ‘true’ for split pricing. Set ‘false’ for pricing
        together.SplitPricing is not supported with post book re-pricing.
    most_restrictive_penalties
        Boolean flag used to request the MostRestrictivePenalties in the
        response
    fare_rule_validation
        A boolean flag used to request host to return the lowest fare which
        matches the specified fare basis code and passes rule validation
    pricing_preference
        An attribute to return the Lowest Price/Ignore availability for a
        booked itinerary with the valid preferences
        "PriceIgnoreAvailability" and "PriceWithAvailability"
    """

    air_itinerary: None | AirItinerary = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        },
    )
    air_pricing_modifiers: None | AirPricingModifiers = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    search_passenger: list[SearchPassenger1] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 18,
        },
    )
    air_pricing_command: list[AirPricingCommand] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingCommand",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 16,
        },
    )
    air_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "AirReservationLocatorCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_length": 5,
            "max_length": 8,
        },
    )
    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    pcc: None | Pcc = field(
        default=None,
        metadata={
            "name": "PCC",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    ssr: list[Ssr1] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        },
    )
    check_obfees: None | str = field(
        default=None,
        metadata={
            "name": "CheckOBFees",
            "type": "Attribute",
        },
    )
    fare_rule_type: TypeFareRuleType = field(
        default=TypeFareRuleType.NONE,
        metadata={
            "name": "FareRuleType",
            "type": "Attribute",
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
    ticket_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TicketDate",
            "type": "Attribute",
        },
    )
    check_flight_details: bool = field(
        default=False,
        metadata={
            "name": "CheckFlightDetails",
            "type": "Attribute",
        },
    )
    return_mm: bool = field(
        default=False,
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
        },
    )
    nscc: None | str = field(
        default=None,
        metadata={
            "name": "NSCC",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        },
    )
    split_pricing: bool = field(
        default=False,
        metadata={
            "name": "SplitPricing",
            "type": "Attribute",
        },
    )
    most_restrictive_penalties: bool = field(
        default=False,
        metadata={
            "name": "MostRestrictivePenalties",
            "type": "Attribute",
        },
    )
    fare_rule_validation: bool = field(
        default=False,
        metadata={
            "name": "FareRuleValidation",
            "type": "Attribute",
        },
    )
    pricing_preference: None | str = field(
        default=None,
        metadata={
            "name": "PricingPreference",
            "type": "Attribute",
        },
    )
