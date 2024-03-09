from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class TerminalCommand:
    """
    The command to pass to the host.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
