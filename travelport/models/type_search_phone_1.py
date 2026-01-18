from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypeSearchPhone1:
    """
    The phone of the profile to search for.

    Parameters
    ----------
    country_code
        The country code of the profile to search for.
    area_code
        The area code of the profile to search for.
    local_number
        The phone number of the profile to search for.
    """

    class Meta:
        name = "typeSearchPhone"

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
    local_number: None | str = field(
        default=None,
        metadata={
            "name": "LocalNumber",
            "type": "Attribute",
            "max_length": 50,
        },
    )
