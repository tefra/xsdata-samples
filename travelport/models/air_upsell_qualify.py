from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_code_1 import AccountCode1
from travelport.models.flight_spec import FlightSpec
from travelport.models.operating_flight_spec import OperatingFlightSpec
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_time_spec_1 import TypeTimeSpec1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AirUpsellQualify:
    """
    Parameters
    ----------
    departure_time
    flight_spec
    operating_flight_spec
    account_code
    carrier
    effective_date
    expiration_date
    provider_code
    origin
    destination
    class_of_service
    operating_carrier
    offer_ref
    key
    fare_basis
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
        namespace = "http://www.travelport.com/schema/util_v52_0"

    departure_time: None | TypeTimeSpec1 = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
        },
    )
    flight_spec: None | FlightSpec = field(
        default=None,
        metadata={
            "name": "FlightSpec",
            "type": "Element",
        },
    )
    operating_flight_spec: None | OperatingFlightSpec = field(
        default=None,
        metadata={
            "name": "OperatingFlightSpec",
            "type": "Element",
        },
    )
    account_code: None | AccountCode1 = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    effective_date: None | str = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    expiration_date: None | str = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
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
    class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
    operating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    offer_ref: None | str = field(
        default=None,
        metadata={
            "name": "OfferRef",
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
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "max_length": 20,
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
