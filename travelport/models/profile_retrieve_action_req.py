from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5
from travelport.models.type_action_ref import TypeActionRef

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveActionReq(BaseReq5):
    """
    Retrieves details of specific Action(s).

    Parameters
    ----------
    action_info
        Action to retrieve.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    action_info: list[TypeActionRef] = field(
        default_factory=list,
        metadata={
            "name": "ActionInfo",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
