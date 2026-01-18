from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class CustomizedNameData4:
    """
    Customized Name Data is used to print customized name on the different
    documents.
    """

    class Meta:
        name = "CustomizedNameData"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
