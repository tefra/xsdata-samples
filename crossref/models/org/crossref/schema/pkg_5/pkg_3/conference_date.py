from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ConferenceDate:
    """
    The start and end dates of a conference event. conference_date may be
    used in three ways: 1.

    If publishers that do not have parsed date values, provide just text
    with the conference dates. The date text should be taken from the
    proceedings title page. 2. If publishers have parsed date values,
    provide them in the attributes. 3. If both parsed date values and the
    date text are available, both should be provided. This is the preferred
    tagging for conference_date. For example: <ns1:conference_date
    xmlns:ns1="http://www.crossref.org/schema/5.3.1" start_month="01"
    start_year="1997" start_day="15" end_year="1997" end_month="01"
    end_day="17">Jan. 15-17, 1997</ns1:conference_date>.
    """

    class Meta:
        name = "conference_date"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 100,
        },
    )
    start_day: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 31,
            "total_digits": 2,
        },
    )
    start_month: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 34,
            "total_digits": 2,
        },
    )
    start_year: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1400,
            "max_inclusive": 2200,
            "total_digits": 4,
        },
    )
    end_day: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 31,
            "total_digits": 2,
        },
    )
    end_month: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 34,
            "total_digits": 2,
        },
    )
    end_year: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1400,
            "max_inclusive": 2200,
            "total_digits": 4,
        },
    )
