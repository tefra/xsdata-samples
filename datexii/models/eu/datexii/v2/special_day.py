from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.public_holiday import PublicHoliday
from datexii.models.eu.datexii.v2.special_day_type_enum import SpecialDayTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SpecialDay:
    """Specification of a special day, for example schoolDay, electionDay, ...

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
    intersect_with_applicable_days: Optional[bool] = field(
        default=None,
        metadata={
            "name": "intersectWithApplicableDays",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    special_day_type: Optional[SpecialDayTypeEnum] = field(
        default=None,
        metadata={
            "name": "specialDayType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    special_day_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "specialDayName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    public_holiday: List[PublicHoliday] = field(
        default_factory=list,
        metadata={
            "name": "publicHoliday",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    special_day_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "specialDayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
