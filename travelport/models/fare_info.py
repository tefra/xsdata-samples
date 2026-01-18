from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.account_code_1 import AccountCode1
from travelport.models.baggage_allowance import BaggageAllowance
from travelport.models.brand import Brand
from travelport.models.commission_1 import Commission1
from travelport.models.contract_code import ContractCode
from travelport.models.endorsement_1 import Endorsement1
from travelport.models.fare_remark_ref import FareRemarkRef
from travelport.models.fare_rule_failure_info import FareRuleFailureInfo
from travelport.models.fare_rule_key import FareRuleKey
from travelport.models.fare_rules_filter import FareRulesFilter
from travelport.models.fare_surcharge import FareSurcharge
from travelport.models.fare_ticket_designator import FareTicketDesignator
from travelport.models.ticketing_code import TicketingCode
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_fare_penalty import TypeFarePenalty
from travelport.models.type_private_fare import TypePrivateFare

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FareInfo:
    """
    Information about this fare component.

    Parameters
    ----------
    fare_ticket_designator
    ticketing_code
    fare_surcharge
    account_code
    contract_code
    endorsement
    baggage_allowance
    fare_rule_key
    fare_rule_failure_info
    fare_remark_ref
    brand
    commission
        Specifies the Commission for Agency for a particular Fare component.
        Apllicable Providers are 1G and 1V.
    fare_attributes
        Returns all fare attributes separated by pipe ‘|’. Attribute
        information is returned by comma separated values for each
        attribute. These information include attribute number, chargeable
        indicator and supplementary info. Attribute numbers: 1 - Checked
        Bag, 2 - Carry On, 3 - Rebooking, 4 - Refund, 5 - Seats, 6 - Meals,
        7 - WiFi. Chargeable Indicator: Y - Chargeable, N - Not Chargeable.
        Supplementary Information that will be returned is : For 1 and 2 -
        Baggage weights. For 3 – Changeable Info. For 4 – Refundable Info.
        For 5 - Seat description. For 6 – Meal description. For 7 – WiFi
        description. Example:
        1,Y,23|1,N,50|2,N,8|3,N,CHANGEABLE|4,Y,REFUNDABLE|5,N,SEATING|5,N,MIDDLE|6,Y,SOFT
        DRINK|6,N,ALCOHOLIC DRINK|6,Y,SNACK|7,X,WIFI
    change_penalty
        The penalty (if any) to change the itinerary
    cancel_penalty
        The penalty (if any) to cancel the fare
    fare_rules_filter
    key
    fare_basis
        The fare basis code for this fare
    passenger_type_code
        The PTC that is associated with this fare.
    origin
        Returns the airport or city code that defines the origin market for
        this fare.
    destination
        Returns the airport or city code that defines the destination market
        for this fare.
    effective_date
        Returns the date on which this fare was quoted
    travel_date
        Returns the departure date of the first segment that uses this fare.
    departure_date
        Returns the departure date of the first segment of the journey.
    amount
    private_fare
    negotiated_fare
        Identifies the fare as a Negotiated Fare.
    tour_code
    waiver_code
    not_valid_before
        Fare not valid before this date.
    not_valid_after
        Fare not valid after this date.
    pseudo_city_code
        Provider PseudoCityCode associated with private fare.
    fare_family
        An alpha-numeric string which denotes fare family. Some carriers may
        return this in lieu of or in addition to the CabinClass.
    promotional_fare
        Boolean to describe whether the Fare is Promotional fare or not.
    car_code
    value_code
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    bulk_ticket
        Whether the ticket can be issued as bulk for this fare. Providers
        supported: Worldspan
    inclusive_tour
        Whether the ticket can be issued as part of included package for
        this fare. Providers supported: Worldspan
    value
        Used in rapid reprice
    supplier_code
        Code of the provider returning this fare info
    tax_amount
        Currency code and value for the approximate tax amount for this fare
        component.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_ticket_designator: list[FareTicketDesignator] = field(
        default_factory=list,
        metadata={
            "name": "FareTicketDesignator",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    ticketing_code: list[TicketingCode] = field(
        default_factory=list,
        metadata={
            "name": "TicketingCode",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_surcharge: list[FareSurcharge] = field(
        default_factory=list,
        metadata={
            "name": "FareSurcharge",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    account_code: list[AccountCode1] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    contract_code: list[ContractCode] = field(
        default_factory=list,
        metadata={
            "name": "ContractCode",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    endorsement: list[Endorsement1] = field(
        default_factory=list,
        metadata={
            "name": "Endorsement",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    baggage_allowance: None | BaggageAllowance = field(
        default=None,
        metadata={
            "name": "BaggageAllowance",
            "type": "Element",
        },
    )
    fare_rule_key: None | FareRuleKey = field(
        default=None,
        metadata={
            "name": "FareRuleKey",
            "type": "Element",
        },
    )
    fare_rule_failure_info: None | FareRuleFailureInfo = field(
        default=None,
        metadata={
            "name": "FareRuleFailureInfo",
            "type": "Element",
        },
    )
    fare_remark_ref: list[FareRemarkRef] = field(
        default_factory=list,
        metadata={
            "name": "FareRemarkRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    brand: None | Brand = field(
        default=None,
        metadata={
            "name": "Brand",
            "type": "Element",
        },
    )
    commission: None | Commission1 = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    fare_attributes: None | str = field(
        default=None,
        metadata={
            "name": "FareAttributes",
            "type": "Element",
        },
    )
    change_penalty: None | TypeFarePenalty = field(
        default=None,
        metadata={
            "name": "ChangePenalty",
            "type": "Element",
        },
    )
    cancel_penalty: None | TypeFarePenalty = field(
        default=None,
        metadata={
            "name": "CancelPenalty",
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
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    fare_basis: str = field(
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
        }
    )
    passenger_type_code: str = field(
        metadata={
            "name": "PassengerTypeCode",
            "type": "Attribute",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        }
    )
    origin: str = field(
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: str = field(
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    effective_date: str = field(
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
        }
    )
    travel_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
        },
    )
    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    private_fare: None | TypePrivateFare = field(
        default=None,
        metadata={
            "name": "PrivateFare",
            "type": "Attribute",
        },
    )
    negotiated_fare: None | bool = field(
        default=None,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
        },
    )
    tour_code: None | str = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
            "max_length": 15,
        },
    )
    waiver_code: None | str = field(
        default=None,
        metadata={
            "name": "WaiverCode",
            "type": "Attribute",
        },
    )
    not_valid_before: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidBefore",
            "type": "Attribute",
        },
    )
    not_valid_after: None | XmlDate = field(
        default=None,
        metadata={
            "name": "NotValidAfter",
            "type": "Attribute",
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    fare_family: None | str = field(
        default=None,
        metadata={
            "name": "FareFamily",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 32,
        },
    )
    promotional_fare: None | bool = field(
        default=None,
        metadata={
            "name": "PromotionalFare",
            "type": "Attribute",
        },
    )
    car_code: None | str = field(
        default=None,
        metadata={
            "name": "CarCode",
            "type": "Attribute",
            "max_length": 15,
        },
    )
    value_code: None | str = field(
        default=None,
        metadata={
            "name": "ValueCode",
            "type": "Attribute",
            "max_length": 15,
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
    bulk_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        },
    )
    inclusive_tour: None | bool = field(
        default=None,
        metadata={
            "name": "InclusiveTour",
            "type": "Attribute",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
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
    tax_amount: None | str = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Attribute",
        },
    )
