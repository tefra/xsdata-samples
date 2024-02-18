from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_4 import BaseReq4
from travelport.models.host_token_3 import HostToken3
from travelport.models.terminal_command import TerminalCommand

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class TerminalReq(BaseReq4):
    """
    Use this request to send a terminal command to a host.

    Parameters
    ----------
    host_token
        A valid host token. This token must be maintained between sucessive
        calls for the same host session.
    terminal_command
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    host_token: None | HostToken3 = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "required": True,
        },
    )
    terminal_command: None | TerminalCommand = field(
        default=None,
        metadata={
            "name": "TerminalCommand",
            "type": "Element",
            "required": True,
        },
    )
