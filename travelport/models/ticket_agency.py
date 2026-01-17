from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TicketAgency:
    """
    This modifier will override the pseudo of the ticketing agency found in
    the AAT (TKAG).

    Used for all plating carrier validation.

    Parameters
    ----------
    provider_code
        The code of the Provider (e.g. 1G, 1P)
    pseudo_city_code
        The PCC of the host system.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    provider_code: None | object = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        },
    )
    pseudo_city_code: None | object = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
        },
    )
