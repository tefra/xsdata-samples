from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeIntegerRestriction1:
    """
    A fully structured address.

    Parameters
    ----------
    min_value
        The minimum value permitted. Leave blank to specify no minimum
        (which allows negative numbers), or specify an explicit posiitve or
        negative number.
    max_value
        The maximum value permitted.
    """

    class Meta:
        name = "typeIntegerRestriction"

    min_value: None | int = field(
        default=None,
        metadata={
            "name": "MinValue",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 999999999,
        },
    )
    max_value: None | int = field(
        default=None,
        metadata={
            "name": "MaxValue",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 999999999,
        },
    )
