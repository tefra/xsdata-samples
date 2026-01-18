from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass(kw_only=True)
class HeaderTypePropertiesProperty:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    key: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
