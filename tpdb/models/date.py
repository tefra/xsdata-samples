from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class Date:
    class Meta:
        name = "date"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )
