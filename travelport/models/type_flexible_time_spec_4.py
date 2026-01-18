from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_time_spec_4 import TypeTimeSpec4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class TypeFlexibleTimeSpec4(TypeTimeSpec4):
    """
    A type which can be used for flexible date/time specification -extends
    the generic type typeTimeSpec to provide extra options for search.

    Parameters
    ----------
    search_extra_days
        Options to search for extra days on top of the specified date
    """

    class Meta:
        name = "typeFlexibleTimeSpec"

    search_extra_days: None | TypeFlexibleTimeSpec4.SearchExtraDays = field(
        default=None,
        metadata={
            "name": "SearchExtraDays",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )

    @dataclass(kw_only=True)
    class SearchExtraDays:
        """
        Parameters
        ----------
        days_before
            Number of days to search before the specified date
        days_after
            Number of days to search after the specified date
        """

        days_before: None | int = field(
            default=None,
            metadata={
                "name": "DaysBefore",
                "type": "Attribute",
            },
        )
        days_after: None | int = field(
            default=None,
            metadata={
                "name": "DaysAfter",
                "type": "Attribute",
            },
        )
