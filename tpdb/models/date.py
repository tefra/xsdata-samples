from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass
class Date:
    class Meta:
        name = "date"

    value: XmlDate | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
