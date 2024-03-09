from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class PaymentPhone1:
    """
    Payment Phone Number.

    Parameters
    ----------
    country
        The phone number's country code
    area_code
        The phone number's area code
    local_number
        The phone number
    extension
        The phone number's extension
    location
        The IATA airport/city code that corresponds to the location of the
        phone number.
    """

    class Meta:
        name = "PaymentPhone"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "max_length": 5,
        },
    )
    area_code: None | str = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 5,
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
    extension: None | str = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 6,
        },
    )
