from dataclasses import dataclass, field
from typing import Optional
from npo.models.media_search_type import MediaSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ScheduleFormType:
    class Meta:
        name = "scheduleFormType"

    searches: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
