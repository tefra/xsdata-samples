from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Month:
    """
    Month of publication.

    The month must be expressed in numeric format rather spelling out the
    name (e.g.. submit "10", not "October"). The month must be expressed
    with a leading zero if it is less than 10 (e.g. submit "05", not "5").
    When a journal issue has both an issue number and a season, the issue
    number should be placed in issue. If the month of publication is not
    known, the season should be placed in month as a two-digit value as
    follows: Season Value Spring 21 Summer 22 Autumn 23 Winter 24 First
    Quarter 31 Second Quarter 32 Third Quarter 33 Fourth Quarter 34 In
    cases when an issue covers multiple months, e.g. "March-April", include
    only the digits for the first month of the range.
    """

    class Meta:
        name = "month"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 34,
            "total_digits": 2,
        },
    )
