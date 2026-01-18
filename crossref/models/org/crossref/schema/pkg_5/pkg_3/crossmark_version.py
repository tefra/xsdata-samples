from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class CrossmarkVersion:
    class Meta:
        name = "crossmark_version"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
