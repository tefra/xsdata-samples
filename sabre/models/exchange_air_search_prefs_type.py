from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.exchange_travel_preferences_tpa_extensions_type import (
    ExchangeTravelPreferencesTpaExtensionsType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ExchangeAirSearchPrefsType:
    """
    Attributes:
        tpa_extensions:
        valid_interline_ticket: Request itins that are validated on base
            of interline ticketing aggrement.
    """

    tpa_extensions: None | ExchangeTravelPreferencesTpaExtensionsType = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    valid_interline_ticket: bool = field(
        default=False,
        metadata={
            "name": "ValidInterlineTicket",
            "type": "Attribute",
        },
    )
