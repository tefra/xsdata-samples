from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeDaysOfOperation:
    class Meta:
        name = "typeDaysOfOperation"

    mon: None | bool = field(
        default=None,
        metadata={
            "name": "Mon",
            "type": "Attribute",
        },
    )
    tue: None | bool = field(
        default=None,
        metadata={
            "name": "Tue",
            "type": "Attribute",
        },
    )
    wed: None | bool = field(
        default=None,
        metadata={
            "name": "Wed",
            "type": "Attribute",
        },
    )
    thu: None | bool = field(
        default=None,
        metadata={
            "name": "Thu",
            "type": "Attribute",
        },
    )
    fri: None | bool = field(
        default=None,
        metadata={
            "name": "Fri",
            "type": "Attribute",
        },
    )
    sat: None | bool = field(
        default=None,
        metadata={
            "name": "Sat",
            "type": "Attribute",
        },
    )
    sun: None | bool = field(
        default=None,
        metadata={
            "name": "Sun",
            "type": "Attribute",
        },
    )
