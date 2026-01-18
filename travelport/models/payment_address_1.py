from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_line_1 import AddressLine1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class PaymentAddress1:
    """
    Payment Details Address.

    Parameters
    ----------
    address_line
    postal
        The postal code of which this address is located.
    country
        The country of which this address is located.
    state
        The state of which this address is located.
    other_state_province
        Alternate freeform state value
    city
        The city of which this address is located.
    """

    class Meta:
        name = "PaymentAddress"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    address_line: list[AddressLine1] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    postal: None | str = field(
        default=None,
        metadata={
            "name": "Postal",
            "type": "Attribute",
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
    state: None | str = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    other_state_province: None | str = field(
        default=None,
        metadata={
            "name": "OtherStateProvince",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
