from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_provider_reservation_detail_5 import TypeProviderReservationDetail5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class ProviderReservationDetail5(TypeProviderReservationDetail5):
    """
    Common element for mentioning provider reservation locator (PNR) details in
    request.
    """
    class Meta:
        name = "ProviderReservationDetail"
        namespace = "http://www.travelport.com/schema/common_v34_0"
