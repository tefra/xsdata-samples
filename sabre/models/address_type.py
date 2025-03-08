from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.address_type_share_market_ind import (
    AddressTypeShareMarketInd,
)
from sabre.models.address_type_share_synch_ind import AddressTypeShareSynchInd
from sabre.models.country_name_type import CountryNameType
from sabre.models.state_prov_type import StateProvType
from sabre.models.street_nmbr_type import StreetNmbrType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class AddressType:
    """
    Attributes:
        street_nmbr: Street Name and Number within the address
        bldg_room: Building name, room, apartment, or suite number.
        address_line:
        city_name: City name eg. Dublin
        postal_code: Post Office Code number.
        county: County Name eg. Fairfax
        state_prov: State name eg. Texas
        country_name: Country name eg. Ireland
        formatted_ind: Specifies if the associated data is formatted or
            not. If true, then it is formatted, if false, then not
            formatted.
        share_synch_ind:
        share_market_ind:
        type_value: Defines the type of address (e.g. home, business,
            other). Refer to OTA Code List Communication Location Type
            (CLT).
    """

    street_nmbr: None | StreetNmbrType = field(
        default=None,
        metadata={
            "name": "StreetNmbr",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    bldg_room: None | str = field(
        default=None,
        metadata={
            "name": "BldgRoom",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 0,
            "max_length": 64,
        },
    )
    address_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 64,
        },
    )
    city_name: None | str = field(
        default=None,
        metadata={
            "name": "CityName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 64,
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    county: None | str = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 32,
        },
    )
    state_prov: None | StateProvType = field(
        default=None,
        metadata={
            "name": "StateProv",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    country_name: None | CountryNameType = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    formatted_ind: bool = field(
        default=False,
        metadata={
            "name": "FormattedInd",
            "type": "Attribute",
        },
    )
    share_synch_ind: None | AddressTypeShareSynchInd = field(
        default=None,
        metadata={
            "name": "ShareSynchInd",
            "type": "Attribute",
        },
    )
    share_market_ind: None | AddressTypeShareMarketInd = field(
        default=None,
        metadata={
            "name": "ShareMarketInd",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
