from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class Credentials2:
    """
    Container to send login id and password on each request.

    Parameters
    ----------
    user_id
        The UserID associated with the entity using this request withing
        this BranchCode.
    """

    class Meta:
        name = "Credentials"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    user_id: str = field(
        metadata={
            "name": "UserId",
            "type": "Attribute",
            "required": True,
            "max_length": 36,
        }
    )
