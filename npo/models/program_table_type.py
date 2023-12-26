from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.program import Program

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ProgramTableType:
    class Meta:
        name = "programTableType"

    program: list[Program] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
