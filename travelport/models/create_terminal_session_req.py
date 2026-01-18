from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_4 import BaseReq4

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass(kw_only=True)
class CreateTerminalSessionReq(BaseReq4):
    """
    Use this request to create a new session If you do not explicitly close
    a session when you are done, the host may hold onto resources (a pnr
    for example) for some indeterminate amount of time.

    Parameters
    ----------
    host
    session_timeout
        Applicable to 1G/1V. Specify Session Timeout value in Milliseconds.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    host: None | str = field(
        default=None,
        metadata={
            "name": "Host",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    session_timeout: None | int = field(
        default=None,
        metadata={
            "name": "SessionTimeout",
            "type": "Attribute",
        },
    )
