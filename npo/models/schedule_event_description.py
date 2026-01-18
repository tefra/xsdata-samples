from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.owner_type_enum import OwnerTypeEnum
from npo.models.textual_type_enum import TextualTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class ScheduleEventDescription:
    class Meta:
        name = "scheduleEventDescription"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    owner: OwnerTypeEnum = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: TextualTypeEnum = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
