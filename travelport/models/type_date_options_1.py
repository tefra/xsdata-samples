from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeDateOptions1:
    """
    Specify a date using different combinations of Day/Month/Year.

    All are optional attributes, although at least one is required.
    """

    class Meta:
        name = "typeDateOptions"

    day: None | str = field(
        default=None,
        metadata={
            "name": "Day",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
    month: None | str = field(
        default=None,
        metadata={
            "name": "Month",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
    year: None | str = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        },
    )
