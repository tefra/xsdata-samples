from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.telephone_type_share_market_ind import (
    TelephoneTypeShareMarketInd,
)
from sabre.models.telephone_type_share_synch_ind import (
    TelephoneTypeShareSynchInd,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TelephoneType:
    """
    Construct for holding a telephone number.

    Attributes:
        share_synch_ind:
        share_market_ind:
        phone_location_type: Refer to OTA Code List Phone Location Type
            (PLT).
        phone_tech_type: Indicates type of technology associated with
            this telephone number, such as Voice, Data, Fax, Pager,
            Mobile, TTY, etc. Refer to OTA Code List Phone Technology
            Type (PTT).
        country_access_code: Code assigned by telecommunications
            authorities for international country access identifier.
        area_city_code: Code assigned for telephones in a specific
            region, city, or area.
        phone_number: Telephone number assigned to a single location.
        extension: Extension to reach a specific party at the phone
            number.
        pin: Additional codes used for pager or telephone access rights.
        formatted_ind: Specifies if the associated data is formatted or
            not. If true, then it is formatted, if false, then not
            formatted.
    """

    share_synch_ind: None | TelephoneTypeShareSynchInd = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        },
    )
    share_market_ind: None | TelephoneTypeShareMarketInd = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        },
    )
    phone_location_type: None | str = field(
        default=None,
        metadata={
            "name": "PhoneLocationType",
            "type": "Attribute",
        },
    )
    phone_tech_type: None | str = field(
        default=None,
        metadata={
            "name": "PhoneTechType",
            "type": "Attribute",
        },
    )
    country_access_code: None | str = field(
        default=None,
        metadata={
            "name": "CountryAccessCode",
            "type": "Attribute",
            "pattern": r"[0-9]{1,3}",
        },
    )
    area_city_code: None | str = field(
        default=None,
        metadata={
            "name": "AreaCityCode",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        },
    )
    phone_number: None | str = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 32,
        },
    )
    extension: None | str = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "pattern": r"[0-9]{1,5}",
        },
    )
    pin: None | str = field(
        default=None,
        metadata={
            "name": "PIN",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    formatted_ind: bool = field(
        default=False,
        metadata={
            "name": "FormattedInd",
            "type": "Attribute",
        },
    )
