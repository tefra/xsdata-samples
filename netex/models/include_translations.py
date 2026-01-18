from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class IncludeTranslations:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
