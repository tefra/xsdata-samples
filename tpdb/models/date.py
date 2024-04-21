from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate


@dataclass
class Date:
    class Meta:
        name = "date"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
