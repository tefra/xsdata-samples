from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.calculate_tax_result import CalculateTaxResult

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class CalculateTaxRsp(BaseRsp1):
    """
    Response containg calculated total of base prices and taxes.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    calculate_tax_result: CalculateTaxResult = field(
        metadata={
            "name": "CalculateTaxResult",
            "type": "Element",
            "required": True,
        }
    )
