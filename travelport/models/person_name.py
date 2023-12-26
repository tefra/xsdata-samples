from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PersonName:
    """
    Customer name field.

    Parameters
    ----------
    first
        Person First Name.
    last
        Person Last Name.
    prefix
        Person Name prefix.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    first: None | str = field(
        default=None,
        metadata={
            "name": "First",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    last: None | str = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        },
    )
    prefix: None | str = field(
        default=None,
        metadata={
            "name": "Prefix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
