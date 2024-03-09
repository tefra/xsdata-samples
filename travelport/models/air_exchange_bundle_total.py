from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_info_1 import AirExchangeInfo1
from travelport.models.penalty_1 import Penalty1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeBundleTotal:
    """
    Total exchange and penalty information for one ticket number.

    Parameters
    ----------
    air_exchange_info
    penalty
        Only used within an AirExchangeQuoteRsp
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_exchange_info: None | AirExchangeInfo1 = field(
        default=None,
        metadata={
            "name": "AirExchangeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
    penalty: list[Penalty1] = field(
        default_factory=list,
        metadata={
            "name": "Penalty",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
