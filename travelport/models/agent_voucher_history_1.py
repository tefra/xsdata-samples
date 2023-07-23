from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AgentVoucherHistory1:
    """
    Agent Voucher Form of Payments.
    """
    class Meta:
        name = "AgentVoucherHistory"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        }
    )
