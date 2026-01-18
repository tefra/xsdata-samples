from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_4 import BaseRsp4
from travelport.models.host_token_3 import HostToken3

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass(kw_only=True)
class CreateTerminalSessionRsp(BaseRsp4):
    """
    The response containing your session token information to use with
    TerminalReq Don't forget to EndSession when done with the HostToken!

    Parameters
    ----------
    host_token
        The host token associated with the session to use on subsequent
        calls to TerminalReq
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
