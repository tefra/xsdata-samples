from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass(kw_only=True)
class BaseFaultTypeErrorCode:
    class Meta:
        global_type = False

    dialect: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
