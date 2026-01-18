from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass(kw_only=True)
class AgentVoucher2:
    """
    Agent Voucher Form of Payments.
    """

    class Meta:
        name = "AgentVoucher"
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"

    number: str = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
