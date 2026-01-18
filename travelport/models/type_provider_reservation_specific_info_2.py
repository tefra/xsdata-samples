from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.operated_by_2 import OperatedBy2
from travelport.models.provider_reservation_info_ref_3 import (
    ProviderReservationInfoRef3,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class TypeProviderReservationSpecificInfo2:
    """
    Parameters
    ----------
    operated_by
        Cross accrual carrier info
    provider_reservation_info_ref
        Tagging provider reservation info with LoyaltyCard.
    provider_reservation_level
        If true means Loyalty card is applied at ProviderReservation level.
    reservation_level
        If true means Loyalty card is applied at Universal Record
        Reservation level e.g. Hotel Reservation, Vehicle Reservation etc.
    """

    class Meta:
        name = "typeProviderReservationSpecificInfo"

    operated_by: list[OperatedBy2] = field(
        default_factory=list,
        metadata={
            "name": "OperatedBy",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
            "max_occurs": 999,
        },
    )
    provider_reservation_info_ref: None | ProviderReservationInfoRef3 = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    provider_reservation_level: None | bool = field(
        default=None,
        metadata={
            "name": "ProviderReservationLevel",
            "type": "Attribute",
        },
    )
    reservation_level: None | bool = field(
        default=None,
        metadata={
            "name": "ReservationLevel",
            "type": "Attribute",
        },
    )
