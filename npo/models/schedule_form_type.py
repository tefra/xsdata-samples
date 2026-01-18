from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_search_type import MediaSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class ScheduleFormType:
    class Meta:
        name = "scheduleFormType"

    searches: None | MediaSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    highlight: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
