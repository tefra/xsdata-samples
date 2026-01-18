from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class DangerousGoodsRegulationsEnum(Enum):
    """
    Types of dangerous goods regulations.

    :cvar ADR: European agreement on the international carriage of
        dangerous goods on road.
    :cvar IATA_ICAO: Regulations covering the international
        transportation of dangerous goods issued by the International
        Air Transport Association and the International Civil Aviation
        Organisation.
    :cvar IMO_IMDG: Regulations regarding the transportation of
        dangerous goods on ocean-going vessels issued by the
        International Maritime Organisation.
    :cvar RAILROAD_DANGEROUS_GOODS_BOOK: International regulations
        concerning the international carriage of dangerous goods by
        rail.
    """

    ADR = "adr"
    IATA_ICAO = "iataIcao"
    IMO_IMDG = "imoImdg"
    RAILROAD_DANGEROUS_GOODS_BOOK = "railroadDangerousGoodsBook"
