from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class SystemTime:
    """
    Identifies the time of the system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    value: str = field(
        default=""
    )
