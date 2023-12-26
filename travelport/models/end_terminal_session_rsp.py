from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_rsp_4 import BaseRsp4

__NAMESPACE__ = "http://www.travelport.com/schema/terminal_v33_0"


@dataclass
class EndTerminalSessionRsp(BaseRsp4):
    """
    An empty response indicates success.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/terminal_v33_0"
