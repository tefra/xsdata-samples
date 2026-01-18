from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.phone_number_type_7 import PhoneNumberType7
from travelport.models.provider_reservation_info_ref_7 import (
    ProviderReservationInfoRef7,
)
from travelport.models.type_element_status_7 import TypeElementStatus7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class PhoneNumber7:
    """
    Consists of type (office, home, fax), location (city code), the country
    code, the number, and an extension.

    Parameters
    ----------
    provider_reservation_info_ref
    key
    type_value
    location
        IATA code for airport or city
    country_code
        Hosts/providers will expect this to be international dialing digits
    area_code
    number
        The local phone number
    extension
    text
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
        name = "PhoneNumber"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    provider_reservation_info_ref: list[ProviderReservationInfoRef7] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    type_value: None | PhoneNumberType7 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    country_code: None | str = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "max_length": 5,
        },
    )
    area_code: None | str = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    number: str = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 83,
        }
    )
    extension: None | str = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    text: None | str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
            "max_length": 1024,
        },
    )
    el_stat: None | TypeElementStatus7 = field(
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
