from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.group import Group
from npo.models.program import Program
from npo.models.segment import Segment

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class EmbedType:
    class Meta:
        name = "embedType"

    title: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    group: None | Group = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    program: None | Program = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    segment: None | Segment = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
