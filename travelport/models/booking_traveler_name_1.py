from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class BookingTravelerName1:
    """
    Complete name fields.

    Parameters
    ----------
    prefix
        Name prefix.
    first
        First Name.
    middle
        Midle name.
    last
        Last Name.
    suffix
        Name suffix.
    """

    class Meta:
        name = "BookingTravelerName"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    prefix: None | str = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        },
    )
    first: None | str = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    middle: None | str = field(
        default=None,
        metadata={
            "name": "Middle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        },
    )
    last: None | str = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    suffix: None | str = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        },
    )
