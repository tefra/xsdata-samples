from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeAtpcoglobalIndicator(Enum):
    """
    Enumeration of ATPCO global indicators.

    Properties
    ----------
    AL
        FareByRule -- All fares incl. EH/TS
    AP
        Via Atlantic Pacific
    AT
        Via Atlantic
    CA
        Within Canada.
    CT
        Circle trip.
    EH
        Within Eastern Hemisphere
    FE
        Far East
    IN
        FareByRule - For int'l incl. AT/PA/WH/CT/RW
    NA
        FareByRule for North America incl US/CA/TB/PV
    PA
        Via Pacific
    PN
        Via Pacific and via North America
    PO
        Via Polar Route.
    RU
        Russia - Area 3
    RW
        Round The World.
    SA
        South Atlantic only
    SP
        Via South Polar Route
    TB
        Trans-border
    TS
        Via Siberia.
    US
        Within the United States.
    WH
        Within Western Hemisphere
    ZZ
        Any Global
    """

    AL = "AL"
    AP = "AP"
    AT = "AT"
    CA = "CA"
    CT = "CT"
    EH = "EH"
    FE = "FE"
    IN = "IN"
    NA = "NA"
    PA = "PA"
    PN = "PN"
    PO = "PO"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SP = "SP"
    TB = "TB"
    TS = "TS"
    US = "US"
    WH = "WH"
    ZZ = "ZZ"
