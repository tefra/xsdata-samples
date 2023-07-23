from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.cabin_class_1 import CabinClass1
from travelport.models.penalty_fare_information import PenaltyFareInformation
from travelport.models.type_atpcoglobal_indicator import TypeAtpcoglobalIndicator
from travelport.models.type_fare_search_option import TypeFareSearchOption
from travelport.models.type_fare_trip_type import TypeFareTripType
from travelport.models.type_fares_indicator import TypeFaresIndicator

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirFareDisplayModifiers:
    """
    Parameters
    ----------
    trip_type
    cabin_class
    penalty_fare_information
        Request Fares with specific Penalty Information.
    fare_search_option
    max_responses
    departure_date
    ticketing_date
    return_date
    base_fare_only
    unrestricted_fares_only
    fares_indicator
        Indicates whether only public fares should be returned or specific
        type of private fares
    currency_type
    include_taxes
    include_estimated_taxes
        Indicates to include estimated taxes i.e. if set to true estimated
        total fare,base fare and taxes would be returned.
    include_surcharges
    global_indicator
    prohibit_min_stay_fares
    prohibit_max_stay_fares
    prohibit_advance_purchase_fares
    prohibit_non_refundable_fares
        Indicates whether it prohibits NonRefundable Fares.
    validated_fares_only
        Indicates that the requested Fares should be Validated Fares only.
        If set to true, then only valid fares will be returned. If set to
        false, both valid and non valid fares will be returned. If not sent,
        then no validation will be done. All fares will be returned.
    prohibit_travel_restricted_fares
        Indicates that the Fares not complying Travel Restrictions and
        Seasonality fare rules are prohibited
    filed_currency
        Represents the filed currency of the fare
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    trip_type: list[TypeFareTripType] = field(
        default_factory=list,
        metadata={
            "name": "TripType",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    cabin_class: None | CabinClass1 = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    penalty_fare_information: None | PenaltyFareInformation = field(
        default=None,
        metadata={
            "name": "PenaltyFareInformation",
            "type": "Element",
        }
    )
    fare_search_option: list[TypeFareSearchOption] = field(
        default_factory=list,
        metadata={
            "name": "FareSearchOption",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    max_responses: int = field(
        default=200,
        metadata={
            "name": "MaxResponses",
            "type": "Attribute",
        }
    )
    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    ticketing_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TicketingDate",
            "type": "Attribute",
        }
    )
    return_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ReturnDate",
            "type": "Attribute",
        }
    )
    base_fare_only: bool = field(
        default=False,
        metadata={
            "name": "BaseFareOnly",
            "type": "Attribute",
        }
    )
    unrestricted_fares_only: bool = field(
        default=False,
        metadata={
            "name": "UnrestrictedFaresOnly",
            "type": "Attribute",
        }
    )
    fares_indicator: None | TypeFaresIndicator = field(
        default=None,
        metadata={
            "name": "FaresIndicator",
            "type": "Attribute",
        }
    )
    currency_type: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        }
    )
    include_taxes: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeTaxes",
            "type": "Attribute",
        }
    )
    include_estimated_taxes: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeEstimatedTaxes",
            "type": "Attribute",
        }
    )
    include_surcharges: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeSurcharges",
            "type": "Attribute",
        }
    )
    global_indicator: None | TypeAtpcoglobalIndicator = field(
        default=None,
        metadata={
            "name": "GlobalIndicator",
            "type": "Attribute",
        }
    )
    prohibit_min_stay_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitMinStayFares",
            "type": "Attribute",
        }
    )
    prohibit_max_stay_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitMaxStayFares",
            "type": "Attribute",
        }
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitAdvancePurchaseFares",
            "type": "Attribute",
        }
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
        }
    )
    validated_fares_only: None | bool = field(
        default=None,
        metadata={
            "name": "ValidatedFaresOnly",
            "type": "Attribute",
        }
    )
    prohibit_travel_restricted_fares: bool = field(
        default=True,
        metadata={
            "name": "ProhibitTravelRestrictedFares",
            "type": "Attribute",
        }
    )
    filed_currency: None | str = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "length": 3,
        }
    )
