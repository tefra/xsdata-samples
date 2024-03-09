from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_4 import BaseRsp4
from travelport.models.terminal_command_response import TerminalCommandResponse

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class TerminalRsp(BaseRsp4):
    """
    The response from the host for a terminal command.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    terminal_command_response: None | TerminalCommandResponse = field(
        default=None,
        metadata={
            "name": "TerminalCommandResponse",
            "type": "Element",
            "required": True,
        },
    )
