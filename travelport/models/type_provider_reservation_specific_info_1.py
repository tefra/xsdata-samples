from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.operated_by_1 import OperatedBy1
from travelport.models.provider_reservation_info_ref_1 import (
    ProviderReservationInfoRef1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class TypeProviderReservationSpecificInfo1:
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

    operated_by: list[OperatedBy1] = field(
        default_factory=list,
        metadata={
            "name": "OperatedBy",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    provider_reservation_info_ref: None | ProviderReservationInfoRef1 = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
