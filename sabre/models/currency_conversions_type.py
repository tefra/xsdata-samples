from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class CurrencyConversionsType:
    conversion: list[CurrencyConversionsType.Conversion] = field(
        default_factory=list,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Conversion:
        """
        Attributes:
            from_value:
            to:
            rate_of_exchange: Exchange rate
        """

        from_value: None | str = field(
            default=None,
            metadata={
                "name": "From",
                "type": "Attribute",
                "pattern": r"[a-zA-Z]{3}",
            },
        )
        to: None | str = field(
            default=None,
            metadata={
                "name": "To",
                "type": "Attribute",
                "pattern": r"[a-zA-Z]{3}",
            },
        )
        rate_of_exchange: None | float = field(
            default=None,
            metadata={
                "name": "RateOfExchange",
                "type": "Attribute",
            },
        )
