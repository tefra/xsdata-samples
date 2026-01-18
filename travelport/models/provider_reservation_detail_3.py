from __future__ import annotations

from dataclasses import dataclass

from travelport.models.type_provider_reservation_detail_3 import (
    TypeProviderReservationDetail3,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class ProviderReservationDetail3(TypeProviderReservationDetail3):
    """
    common element for mentioning provider reservation locator (PNR)
    details in request.
    """

    class Meta:
        name = "ProviderReservationDetail"
        namespace = "http://www.travelport.com/schema/common_v33_0"
