from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_fee_info_1 import TypeFeeInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FeeInfo(TypeFeeInfo1):
    """
    A generic type of fee for those charges which are incurred by the
    passenger, but not necessarily shown on tickets.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
