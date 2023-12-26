from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class RefundRemark5:
    """
    A textual remark displayed in Refund Quote and Refund response.

    Parameters
    ----------
    remark_data
        Actual remark data.
    """

    class Meta:
        name = "RefundRemark"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    remark_data: None | str = field(
        default=None,
        metadata={
            "name": "RemarkData",
            "type": "Element",
            "required": True,
        },
    )
