from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass(kw_only=True)
class BaseFaultTypeDescription:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
