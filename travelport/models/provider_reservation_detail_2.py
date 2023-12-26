from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_provider_reservation_detail_2 import (
    TypeProviderReservationDetail2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class ProviderReservationDetail2(TypeProviderReservationDetail2):
    """
    Common element for mentioning provider reservation locator (PNR) details in
    request.
    """

    class Meta:
        name = "ProviderReservationDetail"
        namespace = "http://www.travelport.com/schema/common_v32_0"
