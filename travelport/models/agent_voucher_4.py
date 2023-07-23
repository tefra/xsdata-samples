from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class AgentVoucher4:
    """
    Agent Voucher Form of Payments.
    """
    class Meta:
        name = "AgentVoucher"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
