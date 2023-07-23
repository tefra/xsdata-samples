from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareRuleCategoryCode(Enum):
    """
    Kestrel Long Fare Rule Category Codes.

    Properties
    ----------
    APP
        Rule App/Other Conditions
    WHO
        Eligibility
    DAY
        Day/Time
    SEA
        Seasonal
    FLT
        Flight App
    ADV
        Advance Res/Tkt
    MIN
        Minimum Stay
    MAX
        Maximum Stay
    STP
        Stopovers
    TRF
        Transfers/Routing
    CMB
        Combinability
    BLA
        Blackouts
    SUR
        Surcharges
    ACC
        Accompanied
    TVL
        Travel Restrictions
    TKT
        Sales Restrictions
    CHG
        Penalties
    HIP
        HIP and Mileage Exceptions
    END
        Ticket Endorsements
    CHD
        Children"s Discounts
    TUC
        Tour Conductor Disc
    AGT
        Agent Discounts
    DSC
        All Other Disc
    MIS
        Misc Fare Tags
    FBR
        Fare By Rule
    GRP
        Groups
    TUR
        Tours
    VAC
        Visit Another Country
    DEP
        Deposits
    VOL
        Voluntary Changes
    IVE
        Involuntary Exchanges
    VOR
        Voluntary Refunds
    IVR
        Involuntary Refunds
    NET
        Negotiated Fares
    OTH
        Other
    """
    APP = "APP"
    WHO = "WHO"
    DAY = "DAY"
    SEA = "SEA"
    FLT = "FLT"
    ADV = "ADV"
    MIN = "MIN"
    MAX = "MAX"
    STP = "STP"
    TRF = "TRF"
    CMB = "CMB"
    BLA = "BLA"
    SUR = "SUR"
    ACC = "ACC"
    TVL = "TVL"
    TKT = "TKT"
    CHG = "CHG"
    HIP = "HIP"
    END = "END"
    CHD = "CHD"
    TUC = "TUC"
    AGT = "AGT"
    DSC = "DSC"
    MIS = "MIS"
    FBR = "FBR"
    GRP = "GRP"
    TUR = "TUR"
    VAC = "VAC"
    DEP = "DEP"
    VOL = "VOL"
    IVE = "IVE"
    VOR = "VOR"
    IVR = "IVR"
    NET = "NET"
    OTH = "OTH"
