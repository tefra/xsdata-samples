from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TravelerCountType:
    """
    Defines the number of travelers of a specific type (e.g. a driver type can be
    either one of: Adult, YoungDriver, YoungerDriver, or it may be a code that is
    acceptable to both Trading Partners).

    Attributes:
        age:
        code: Specify traveler type code.
        code_context: Identifies the source authority for the code.
        uri: Identifies the location of the code table
        quantity: Used to define a quantity of an associated element or
            attribute.
    """

    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    code_context: None | str = field(
        default=None,
        metadata={
            "name": "CodeContext",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    uri: None | str = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 999,
        },
    )
