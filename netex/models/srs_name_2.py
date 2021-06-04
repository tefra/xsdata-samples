from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SrsName2:
    class Meta:
        name = "SrsName"
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
