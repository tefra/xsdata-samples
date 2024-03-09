from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypeRemark6:
    """
    Parameters
    ----------
    value
    provider_reservation_info_ref
        Provider reservation reference key.
    provider_code
        Contains the Provider Code of the provider for which this element is
        used
    """

    class Meta:
        name = "typeRemark"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
