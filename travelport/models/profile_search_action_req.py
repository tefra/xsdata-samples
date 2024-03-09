from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_5 import BaseReq5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileSearchActionReq(BaseReq5):
    """
    Get summary of all Action(s) available in the system.

    Parameters
    ----------
    consuming_system
        Action Consuming System (Universal Desktop, 3rd party system).
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    consuming_system: None | str = field(
        default=None,
        metadata={
            "name": "ConsumingSystem",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
