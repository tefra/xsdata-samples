from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_provider_reservation_detail_1 import (
    TypeProviderReservationDetail1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class ProviderReservationDetail1(TypeProviderReservationDetail1):
    """
    common element for mentioning provider reservation locator (PNR)
    details in request.
    """

    class Meta:
        name = "ProviderReservationDetail"
        namespace = "http://www.travelport.com/schema/common_v52_0"
