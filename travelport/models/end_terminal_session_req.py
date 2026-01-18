from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_4 import BaseReq4
from travelport.models.host_token_3 import HostToken3

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass(kw_only=True)
class EndTerminalSessionReq(BaseReq4):
    """
    Use this request to close a session you no longer need.

    Parameters
    ----------
    host_token
        The host token for the session you wish to close
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"

    host_token: HostToken3 = field(
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "required": True,
        }
    )
