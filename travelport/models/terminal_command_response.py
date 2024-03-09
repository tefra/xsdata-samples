from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_text_block_2 import TypeTextBlock2

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class TerminalCommandResponse(TypeTextBlock2):
    """The response from the host.

    Usually pre-formatted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"
