from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.phone_number_history_type_1 import (
    PhoneNumberHistoryType1,
)
from travelport.models.provider_reservation_info_ref_2 import (
    ProviderReservationInfoRef2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class PhoneNumberHistory1:
    """
    Consists of type (office, home, fax), location (city code), the country code,
    the number, and an extension.

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
    """

    class Meta:
        name = "PhoneNumberHistory"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    provider_reservation_info_ref: list[ProviderReservationInfoRef2] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    type_value: None | PhoneNumberHistoryType1 = field(
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
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 83,
        },
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
