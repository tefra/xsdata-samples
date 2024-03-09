from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_modifiers import AirExchangeModifiers
from travelport.models.air_pricing_modifiers import AirPricingModifiers
from travelport.models.base_air_search_req import BaseAirSearchReq
from travelport.models.enumeration import Enumeration
from travelport.models.fare_rules_filter_category import (
    FareRulesFilterCategory,
)
from travelport.models.flex_explore_modifiers import FlexExploreModifiers
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.pcc import Pcc
from travelport.models.search_passenger_1 import SearchPassenger1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaseLowFareSearchReq(BaseAirSearchReq):
    """
    Base Low Fare Search Request.

    Parameters
    ----------
    search_passenger
        Provider: 1G,1V,1P,ACH-Maxinumber of passenger increased in to 18 to
        support 9 INF passenger along with 9 ADT,CHD,INS
        passenger
    air_pricing_modifiers
        Provider: 1G,1V,1P,ACH.
    enumeration
        Provider: 1G,1V,1P,ACH.
    air_exchange_modifiers
        Provider: ACH.
    flex_explore_modifiers
        This is the container for a set of modifiers which allow the user to
        perform a special kind of low fare search, depicted as flex explore,
        based on different parameters like Area, Zone, Country, State,
        Specific locations, Distance around the actual destination of the
        itinerary. Applicable for providers 1G,1V,1P.
    pcc
    fare_rules_filter_category
    form_of_payment
        Provider: 1P
    enable_point_to_point_search
        Provider: 1G,1V,1P,ACH-Indicates that low cost providers should be
        queried for top connection options and the results returned with the
        search.
    enable_point_to_point_alternates
        Provider: 1G,1V,1P,ACH-Indicates that suggestions for alternate
        connection cities for low cost providers should be returned with the
        search.
    max_number_of_expert_solutions
        Provider: 1G,1V,1P,ACH-Indicates the Maximum Number of Expert
        Solutions to be returned from the Knowledge Base for the provided
        search criteria
    solution_result
        Provider: 1G,1V,1P,ACH-Indicates whether the response will contain
        Solution result (AirPricingSolution) or Non Solution Result
        (AirPricingPoints). The default value is false. This attribute
        cannot be combined with EnablePointToPointSearch,
        EnablePointToPointAlternates and MaxNumberOfExpertSolutions.
    prefer_complete_itinerary
        Provider: ACH-This attribute is only supported for ACH .It works in
        conjunction with the @SolutionResult flag
    meta_option_identifier
        Invoke Meta Search.  Valid values are 00 to 99, or D for the default
        meta search configuration.  When Meta Search not requested, normal
        LowFareSearch applies.  Supported Providers;  1g/1v/1p
    return_upsell_fare
        When set to “true”, Upsell information will be returned in the shop
        response. Provider supported : 1G, 1V, 1P
    include_fare_info_messages
        Set to True to return FareInfoMessageList. Providers supported:
        1G/1V/1P
    return_branded_fares
        When ReturnBrandedFares is set to “false”, Rich Content and Branding
        will not be returned in the shop response.  When ReturnBrandedFares
        it is set to “true” or is not sent, Rich Content and Branding will
        be returned in the shop response.  Provider: 1P/ACH.
    multi_gdssearch
        A "true" value indicates MultiGDSSearch. Specific provisioning is
        required.
    return_mm
        If this attribute is set to “true”, Fare Control Manager processing
        will be invoked.
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
    nscc
        1 to 3 numeric that defines a Search Control Console filter.This
        attribute is used to override that filter.
    fare_info_rules
        Returns ChangePenalty and CancelPenalty values at the FareInfo
        level. If FareRulesFilterCategory is sent FareRulesFilter will be
        returned at FareInfo level.  Provider: 1G/1V.
    most_restrictive_penalties
        Boolean flag used to request the MostRestrictivePenalties in the
        response
    """

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
    air_pricing_modifiers: None | AirPricingModifiers = field(
        default=None,
        metadata={
            "name": "AirPricingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    enumeration: None | Enumeration = field(
        default=None,
        metadata={
            "name": "Enumeration",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    air_exchange_modifiers: None | AirExchangeModifiers = field(
        default=None,
        metadata={
            "name": "AirExchangeModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    flex_explore_modifiers: None | FlexExploreModifiers = field(
        default=None,
        metadata={
            "name": "FlexExploreModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
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
    fare_rules_filter_category: None | FareRulesFilterCategory = field(
        default=None,
        metadata={
            "name": "FareRulesFilterCategory",
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
            "max_occurs": 99,
        },
    )
    enable_point_to_point_search: bool = field(
        default=False,
        metadata={
            "name": "EnablePointToPointSearch",
            "type": "Attribute",
        },
    )
    enable_point_to_point_alternates: bool = field(
        default=False,
        metadata={
            "name": "EnablePointToPointAlternates",
            "type": "Attribute",
        },
    )
    max_number_of_expert_solutions: int = field(
        default=0,
        metadata={
            "name": "MaxNumberOfExpertSolutions",
            "type": "Attribute",
        },
    )
    solution_result: bool = field(
        default=False,
        metadata={
            "name": "SolutionResult",
            "type": "Attribute",
        },
    )
    prefer_complete_itinerary: bool = field(
        default=True,
        metadata={
            "name": "PreferCompleteItinerary",
            "type": "Attribute",
        },
    )
    meta_option_identifier: None | str = field(
        default=None,
        metadata={
            "name": "MetaOptionIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
    return_upsell_fare: bool = field(
        default=False,
        metadata={
            "name": "ReturnUpsellFare",
            "type": "Attribute",
        },
    )
    include_fare_info_messages: bool = field(
        default=False,
        metadata={
            "name": "IncludeFareInfoMessages",
            "type": "Attribute",
        },
    )
    return_branded_fares: bool = field(
        default=True,
        metadata={
            "name": "ReturnBrandedFares",
            "type": "Attribute",
        },
    )
    multi_gdssearch: bool = field(
        default=False,
        metadata={
            "name": "MultiGDSSearch",
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
    check_obfees: None | str = field(
        default=None,
        metadata={
            "name": "CheckOBFees",
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
    fare_info_rules: bool = field(
        default=False,
        metadata={
            "name": "FareInfoRules",
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
