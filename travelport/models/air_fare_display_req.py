from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_code_1 import AccountCode1
from travelport.models.air_fare_display_modifiers import (
    AirFareDisplayModifiers,
)
from travelport.models.air_fare_display_rule_key import AirFareDisplayRuleKey
from travelport.models.base_req_1 import BaseReq1
from travelport.models.booking_code import BookingCode
from travelport.models.carrier_1 import Carrier1
from travelport.models.contract_code import ContractCode
from travelport.models.fare_basis import FareBasis
from travelport.models.fare_type import FareType
from travelport.models.include_addl_booking_code_info import (
    IncludeAddlBookingCodeInfo,
)
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.type_mile_or_route_based_fare import (
    TypeMileOrRouteBasedFare,
)
from travelport.models.type_passenger_type_1 import TypePassengerType1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirFareDisplayReq(BaseReq1):
    """
    Request to display a tariff for based on origin, destination, and other
    options.

    Parameters
    ----------
    fare_type
        Provider: 1G,1V,1P.
    passenger_type
        Provider: 1G,1V,1P.
    booking_code
        Provider: 1G,1V,1P.
    include_addl_booking_code_info
        Provider: 1G,1V,1P.
    fare_basis
        Provider: 1G,1V,1P.
    carrier
        Provider: 1G,1V,1P.
    account_code
        Provider: 1G,1V,1P.
    contract_code
        Provider: 1G,1V.
    air_fare_display_modifiers
        Provider: 1G,1V,1P.
    point_of_sale
        Provider: 1G,1V.
    air_fare_display_rule_key
        Provider: 1G,1V,1P.
    origin
        Provider: 1G,1V,1P.
    destination
        Provider: 1G,1V,1P.
    provider_code
        Provider: 1G,1V,1P.
    include_mile_route_information
        Provider: 1G,1V,1P-Used to request Mile/Route Information in follow
        on (Mile, Route, Both)
    un_saleable_fares_only
        Provider: 1G,1V,1P-Used to request unsaleable fares only also known
        as place of sale fares.
    channel_id
        A Channel ID is 4 alpha-numeric characters used to activate the
        Search Control Console filter for a specific group of travelers
        being served by the agency credential.
    nscc
        1 to 3 numeric that define a Search Control Console filter.This
        attribute is used to override that filter.
    return_mm
        If this attribute is set to true, Fare Control Manager processing
        will be invoked.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_type: list[FareType] = field(
        default_factory=list,
        metadata={
            "name": "FareType",
            "type": "Element",
            "max_occurs": 5,
        },
    )
    passenger_type: list[TypePassengerType1] = field(
        default_factory=list,
        metadata={
            "name": "PassengerType",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    booking_code: list[BookingCode] = field(
        default_factory=list,
        metadata={
            "name": "BookingCode",
            "type": "Element",
            "max_occurs": 5,
        },
    )
    include_addl_booking_code_info: None | IncludeAddlBookingCodeInfo = field(
        default=None,
        metadata={
            "name": "IncludeAddlBookingCodeInfo",
            "type": "Element",
        },
    )
    fare_basis: None | FareBasis = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Element",
        },
    )
    carrier: list[Carrier1] = field(
        default_factory=list,
        metadata={
            "name": "Carrier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 10,
        },
    )
    account_code: list[AccountCode1] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        },
    )
    contract_code: None | ContractCode = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Element",
        },
    )
    air_fare_display_modifiers: None | AirFareDisplayModifiers = field(
        default=None,
        metadata={
            "name": "AirFareDisplayModifiers",
            "type": "Element",
        },
    )
    point_of_sale: list[PointOfSale1] = field(
        default_factory=list,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 5,
        },
    )
    air_fare_display_rule_key: None | AirFareDisplayRuleKey = field(
        default=None,
        metadata={
            "name": "AirFareDisplayRuleKey",
            "type": "Element",
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    include_mile_route_information: None | TypeMileOrRouteBasedFare = field(
        default=None,
        metadata={
            "name": "IncludeMileRouteInformation",
            "type": "Attribute",
        },
    )
    un_saleable_fares_only: None | bool = field(
        default=None,
        metadata={
            "name": "UnSaleableFaresOnly",
            "type": "Attribute",
        },
    )
    channel_id: None | str = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 4,
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
    return_mm: bool = field(
        default=False,
        metadata={
            "name": "ReturnMM",
            "type": "Attribute",
        },
    )
