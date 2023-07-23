from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeFloatRestriction2:
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
        name = "typeFloatRestriction"

    min_value: None | float = field(
        default=None,
        metadata={
            "name": "MinValue",
            "type": "Attribute",
            "max_inclusive": 9999999.0,
        }
    )
    max_value: None | float = field(
        default=None,
        metadata={
            "name": "MaxValue",
            "type": "Attribute",
            "max_inclusive": 9999999.0,
        }
    )
