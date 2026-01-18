from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.group import Group

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class GroupTableType:
    class Meta:
        name = "groupTableType"

    group: list[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        },
    )
