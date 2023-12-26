from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeStringRestriction2:
    """Restrictions on profile data for fields with a data type of string.

    Min and max lengths are inclusive.

    Parameters
    ----------
    enumeration
        A specific value permitted.
    min_length
        The minimum length permitted.
    max_length
        The maximum length permitted.
    """

    class Meta:
        name = "typeStringRestriction"

    enumeration: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Enumeration",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
            "min_length": 1,
            "max_length": 128,
            "white_space": "collapse",
        },
    )
    min_length: None | int = field(
        default=None,
        metadata={
            "name": "MinLength",
            "type": "Attribute",
        },
    )
    max_length: None | int = field(
        default=None,
        metadata={
            "name": "MaxLength",
            "type": "Attribute",
        },
    )
