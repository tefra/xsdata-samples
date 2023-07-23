from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class TerminalSessionInfo2:
    """Travelport use only.

    This element contains CDATA information representing existing GDS
    session data or ACH credentials information of the terminal user
    """
    class Meta:
        name = "TerminalSessionInfo"
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
