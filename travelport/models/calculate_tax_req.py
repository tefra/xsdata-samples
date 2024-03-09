from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.tax_calc_info import TaxCalcInfo

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class CalculateTaxReq(BaseReq1):
    """
    Request to calculate US taxes based on a series of segments.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    tax_calc_info: list[TaxCalcInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxCalcInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
