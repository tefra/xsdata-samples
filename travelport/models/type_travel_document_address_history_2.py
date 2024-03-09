from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_line_2 import AddressLine2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeTravelDocumentAddressHistory2:
    """
    Profile Address.

    Parameters
    ----------
    address_line
    state
        The state of which this address is located.
    other_state_province
        Alternate freeform state value
    country
        The country of which this address is located.
    postal
        The postal code of which this address is located.
    city
        The city of which this address is located.
    """

    class Meta:
        name = "typeTravelDocumentAddressHistory"

    address_line: list[AddressLine2] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 3,
        },
    )
    state: None | str = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
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
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
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
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Attribute",
            "max_length": 128,
        },
    )
