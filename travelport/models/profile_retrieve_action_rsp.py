from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.action import Action
from travelport.models.base_rsp_5 import BaseRsp5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileRetrieveActionRsp(BaseRsp5):
    """
    Response containing details of retrieved action(s).

    Parameters
    ----------
    action
        Details of each action.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    action: list[Action] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
            "max_occurs": 999,
        },
    )
