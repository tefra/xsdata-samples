from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.award_shopping_type import AwardShoppingType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ExchangeTpaExtensionsType:
    class Meta:
        name = "ExchangeTPA_ExtensionsType"

    award_shopping: None | AwardShoppingType = field(
        default=None,
        metadata={
            "name": "AwardShopping",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
