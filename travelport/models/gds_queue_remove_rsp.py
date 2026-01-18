from __future__ import annotations

from dataclasses import dataclass

from travelport.models.base_rsp_1 import BaseRsp1

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass(kw_only=True)
class GdsQueueRemoveRsp(BaseRsp1):
    """
    An empty response indicates success.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"
