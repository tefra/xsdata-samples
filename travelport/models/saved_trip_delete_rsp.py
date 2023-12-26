from __future__ import annotations
from dataclasses import dataclass
from travelport.models.base_rsp_1 import BaseRsp1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripDeleteRsp(BaseRsp1):
    """
    Response to delete saved Trip.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"
