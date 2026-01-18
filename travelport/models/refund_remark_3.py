from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class RefundRemark3:
    """
    A textual remark displayed in Refund Quote and Refund response.

    Parameters
    ----------
    remark_data
        Actual remark data.
    """

    class Meta:
        name = "RefundRemark"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    remark_data: str = field(
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "required": True,
        }
    )
