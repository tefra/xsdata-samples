from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeSearchAddress1:
    """
    The address of the profile to search for.

    Parameters
    ----------
    address_line
        Street (must match exactly one of the streets)
    city
        The city of the profile to search for.
    state_province
        The state/province of the profile to search for.
    postal_code
        The postal code of the profile to search for.
    country
        The country of the profile to search for.
    """

    class Meta:
        name = "typeSearchAddress"

    address_line: None | str = field(
        default=None,
        metadata={
            "name": "AddressLine",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 50,
        },
    )
    state_province: None | str = field(
        default=None,
        metadata={
            "name": "StateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
            "white_space": "collapse",
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 12,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "length": 2,
        },
    )
