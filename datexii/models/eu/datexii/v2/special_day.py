from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.public_holiday import PublicHoliday
from datexii.models.eu.datexii.v2.special_day_type_enum import (
    SpecialDayTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class SpecialDay:
    """
    Specification of a special day, for example schoolDay, electionDay, ...

    Gives also the possibility to define a public holiday (country
    specific).

    :ivar intersect_with_applicable_days: When true, the period is the
        intersection of applicable days and this special day. When
        false, the period is the union of applicable days and this
        special day.”
    :ivar special_day_type: Specification of a special day, for example
        schoolDay, electionDay, ..  .
    :ivar special_day_name: Specification of a special day, if the
        enumeration values do not fit.
    :ivar public_holiday:
    :ivar special_day_extension:
    """

    intersect_with_applicable_days: bool = field(
        metadata={
            "name": "intersectWithApplicableDays",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    special_day_type: SpecialDayTypeEnum = field(
        metadata={
            "name": "specialDayType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    special_day_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "specialDayName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    public_holiday: list[PublicHoliday] = field(
        default_factory=list,
        metadata={
            "name": "publicHoliday",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    special_day_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "specialDayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
