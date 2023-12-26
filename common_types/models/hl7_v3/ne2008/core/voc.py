from enum import Enum

__NAMESPACE__ = "urn:hl7-org:v3"


class AcknowledgementDetailType(Enum):
    """vocSet: T19358 (C-0-T19358-cpt)"""

    E = "E"
    I = "I"
    W = "W"


class ActClass(Enum):
    """vocSet: T11527 (C-0-T11527-cpt)"""

    PCPR = "PCPR"
    ENC = "ENC"
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"
    COMPOSITION = "COMPOSITION"
    ENTRY = "ENTRY"
    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"
    EXTRACT = "EXTRACT"
    EHR = "EHR"
    ORGANIZER = "ORGANIZER"
    CATEGORY = "CATEGORY"
    DOCBODY = "DOCBODY"
    DOCSECT = "DOCSECT"
    TOPIC = "TOPIC"
    FOLDER = "FOLDER"
    FCNTRCT = "FCNTRCT"
    COV = "COV"
    CNTRCT = "CNTRCT"
    CACT = "CACT"
    ACTN = "ACTN"
    INFO = "INFO"
    STC = "STC"
    EXPOS = "EXPOS"
    AEXPOS = "AEXPOS"
    TEXPOS = "TEXPOS"
    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"
    GEN = "GEN"
    SEQ = "SEQ"
    SEQVAR = "SEQVAR"
    DETPOL = "DETPOL"
    EXP = "EXP"
    LOC = "LOC"
    PHN = "PHN"
    POL = "POL"
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    SFWL = "SFWL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SIT = "SIT"
    STN = "STN"
    IMAGING_SUBJECT_ORIENTATION = "_ImagingSubjectOrientation"
    OBS = "OBS"
    CNOD = "CNOD"
    VERIF = "VERIF"
    CLNTRL = "CLNTRL"
    ALRT = "ALRT"
    DGIMG = "DGIMG"
    INVSTG = "INVSTG"
    SPCOBS = "SPCOBS"
    POLICY = "POLICY"
    JURISPOL = "JURISPOL"
    ORGPOL = "ORGPOL"
    SCOPOL = "SCOPOL"
    STDPOL = "STDPOL"
    PROC = "PROC"
    SPECCOLLECT = "SPECCOLLECT"
    SPLY = "SPLY"
    DIET = "DIET"
    ACT = "ACT"
    SUBST = "SUBST"
    ACSN = "ACSN"
    ACCM = "ACCM"
    ACCT = "ACCT"
    CTTEVENT = "CTTEVENT"
    CONS = "CONS"
    CONTREG = "CONTREG"
    DISPACT = "DISPACT"
    ADJUD = "ADJUD"
    XACT = "XACT"
    INC = "INC"
    INFRM = "INFRM"
    INVE = "INVE"
    MPROT = "MPROT"
    REG = "REG"
    REV = "REV"
    SPCTRT = "SPCTRT"
    SBADM = "SBADM"
    TRFR = "TRFR"
    TRNS = "TRNS"
    LIST = "LIST"


class ActClassCareProvision(Enum):
    """specDomain: S18964 (C-0-T11527-S13856-S18964-cpt)"""

    PCPR = "PCPR"
    ENC = "ENC"


class ActClassClinicalDocument(Enum):
    """specDomain: S13948 (C-0-T11527-S13856-A19445-S20083-S18938-S13948-cpt)"""

    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"


class ActClassCondition(Enum):
    """specDomain: S18862 (C-0-T11527-S13856-S11529-S18862-cpt)"""

    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"


class ActClassContainer(Enum):
    """abstDomain: A19445 (C-0-T11527-S13856-A19445-cpt)"""

    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"
    COMPOSITION = "COMPOSITION"
    ENTRY = "ENTRY"
    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"
    EXTRACT = "EXTRACT"
    EHR = "EHR"
    ORGANIZER = "ORGANIZER"
    CATEGORY = "CATEGORY"
    DOCBODY = "DOCBODY"
    DOCSECT = "DOCSECT"
    TOPIC = "TOPIC"
    FOLDER = "FOLDER"


class ActClassContract(Enum):
    """specDomain: S14002 (C-0-T11527-S13856-S14002-cpt)"""

    FCNTRCT = "FCNTRCT"
    COV = "COV"
    CNTRCT = "CNTRCT"


class ActClassControlAct(Enum):
    """specDomain: S11534 (C-0-T11527-S13856-S11534-cpt)"""

    CACT = "CACT"
    ACTN = "ACTN"
    INFO = "INFO"
    STC = "STC"


class ActClassDocument(Enum):
    """specDomain: S18938 (C-0-T11527-S13856-A19445-S20083-S18938-cpt)"""

    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"


class ActClassObservation(Enum):
    """specDomain: S11529 (C-0-T11527-S13856-S11529-cpt)"""

    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"
    GEN = "GEN"
    SEQ = "SEQ"
    SEQVAR = "SEQVAR"
    DETPOL = "DETPOL"
    EXP = "EXP"
    LOC = "LOC"
    PHN = "PHN"
    POL = "POL"
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    SFWL = "SFWL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SIT = "SIT"
    STN = "STN"
    IMAGING_SUBJECT_ORIENTATION = "_ImagingSubjectOrientation"
    OBS = "OBS"
    CNOD = "CNOD"
    VERIF = "VERIF"
    CLNTRL = "CLNTRL"
    ALRT = "ALRT"
    DGIMG = "DGIMG"
    INVSTG = "INVSTG"
    SPCOBS = "SPCOBS"


class ActClassPosition(Enum):
    """specDomain: S21646 (C-0-T11527-S13856-S11529-S21646-cpt)"""

    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"


class ActClassProcedure(Enum):
    """specDomain: S11532 (C-0-T11527-S13856-S11532-cpt)"""

    PROC = "PROC"
    SPECCOLLECT = "SPECCOLLECT"


class ActClassRoot(Enum):
    """specDomain: S13856 (C-0-T11527-S13856-cpt)"""

    PCPR = "PCPR"
    ENC = "ENC"
    DOCCLIN = "DOCCLIN"
    CDALVLONE = "CDALVLONE"
    DOC = "DOC"
    COMPOSITION = "COMPOSITION"
    ENTRY = "ENTRY"
    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"
    EXTRACT = "EXTRACT"
    EHR = "EHR"
    ORGANIZER = "ORGANIZER"
    CATEGORY = "CATEGORY"
    DOCBODY = "DOCBODY"
    DOCSECT = "DOCSECT"
    TOPIC = "TOPIC"
    FOLDER = "FOLDER"
    FCNTRCT = "FCNTRCT"
    COV = "COV"
    CNTRCT = "CNTRCT"
    CACT = "CACT"
    ACTN = "ACTN"
    INFO = "INFO"
    STC = "STC"
    EXPOS = "EXPOS"
    AEXPOS = "AEXPOS"
    TEXPOS = "TEXPOS"
    CASE = "CASE"
    OUTB = "OUTB"
    COND = "COND"
    GEN = "GEN"
    SEQ = "SEQ"
    SEQVAR = "SEQVAR"
    DETPOL = "DETPOL"
    EXP = "EXP"
    LOC = "LOC"
    PHN = "PHN"
    POL = "POL"
    OBSSER = "OBSSER"
    OBSCOR = "OBSCOR"
    POS = "POS"
    POSACC = "POSACC"
    POSCOORD = "POSCOORD"
    ROIBND = "ROIBND"
    ROIOVL = "ROIOVL"
    SUP = "SUP"
    RTRD = "RTRD"
    TRD = "TRD"
    SFWL = "SFWL"
    LLD = "LLD"
    PRN = "PRN"
    RLD = "RLD"
    SIT = "SIT"
    STN = "STN"
    IMAGING_SUBJECT_ORIENTATION = "_ImagingSubjectOrientation"
    OBS = "OBS"
    CNOD = "CNOD"
    VERIF = "VERIF"
    CLNTRL = "CLNTRL"
    ALRT = "ALRT"
    DGIMG = "DGIMG"
    INVSTG = "INVSTG"
    SPCOBS = "SPCOBS"
    POLICY = "POLICY"
    JURISPOL = "JURISPOL"
    ORGPOL = "ORGPOL"
    SCOPOL = "SCOPOL"
    STDPOL = "STDPOL"
    PROC = "PROC"
    SPECCOLLECT = "SPECCOLLECT"
    SPLY = "SPLY"
    DIET = "DIET"
    ACT = "ACT"
    SUBST = "SUBST"
    ACSN = "ACSN"
    ACCM = "ACCM"
    ACCT = "ACCT"
    CTTEVENT = "CTTEVENT"
    CONS = "CONS"
    CONTREG = "CONTREG"
    DISPACT = "DISPACT"
    ADJUD = "ADJUD"
    XACT = "XACT"
    INC = "INC"
    INFRM = "INFRM"
    INVE = "INVE"
    MPROT = "MPROT"
    REG = "REG"
    REV = "REV"
    SPCTRT = "SPCTRT"
    SBADM = "SBADM"
    TRFR = "TRFR"
    TRNS = "TRNS"
    LIST = "LIST"


class ActClassSupply(Enum):
    """specDomain: S11535 (C-0-T11527-S13856-S11535-cpt)"""

    SPLY = "SPLY"
    DIET = "DIET"


class ActMood(Enum):
    """vocSet: T10196 (C-0-T10196-cpt)"""

    PRP = "PRP"
    RMD = "RMD"
    INT = "INT"
    APT = "APT"
    ARQ = "ARQ"
    PRMS = "PRMS"
    RQO = "RQO"
    SLOT = "SLOT"
    DEF = "DEF"
    EVN = "EVN"
    CRT = "CRT"
    EVN_CRT = "EVN.CRT"
    GOL = "GOL"
    EXPEC = "EXPEC"
    OPT = "OPT"
    PERM = "PERM"
    PERMRQ = "PERMRQ"
    RSK = "RSK"


class ActMoodCompletionTrack(Enum):
    """abstDomain: A10197 (C-0-T10196-A10197-cpt)"""

    PRP = "PRP"
    RMD = "RMD"
    INT = "INT"
    APT = "APT"
    ARQ = "ARQ"
    PRMS = "PRMS"
    RQO = "RQO"
    SLOT = "SLOT"
    DEF = "DEF"
    EVN = "EVN"


class ActMoodCriterion(Enum):
    """specDomain: S22042 (C-0-T10196-A10202-S22042-cpt)"""

    CRT = "CRT"
    EVN_CRT = "EVN.CRT"


class ActMoodIntent(Enum):
    """specDomain: S10199 (C-0-T10196-A10197-S10199-cpt)"""

    PRP = "PRP"
    RMD = "RMD"
    INT = "INT"
    APT = "APT"
    ARQ = "ARQ"
    PRMS = "PRMS"
    RQO = "RQO"
    SLOT = "SLOT"


class ActRelationshipConditional(Enum):
    """abstDomain: A18977 (C-0-T10317-A18977-cpt)"""

    MITGT = "MITGT"
    RCVY = "RCVY"
    RSON = "RSON"
    BLOCK = "BLOCK"
    CURE_ADJ = "CURE.ADJ"
    MTGT_ADJ = "MTGT.ADJ"
    CURE = "CURE"
    DIAG = "DIAG"
    SYMP = "SYMP"
    CIND = "CIND"
    PRCN = "PRCN"
    TRIG = "TRIG"


class ActRelationshipCostTracking(Enum):
    """abstDomain: A19610 (C-0-T10317-S10329-A14900-A19610-cpt)"""

    CHRG = "CHRG"
    COST = "COST"


class ActRelationshipFulfills(Enum):
    """specDomain: S10342 (C-0-T10317-S10337-S10342-cpt)"""

    FLFS = "FLFS"
    OCCR = "OCCR"
    OREF = "OREF"
    SCH = "SCH"


class ActRelationshipHasComponent(Enum):
    """specDomain: S10318 (C-0-T10317-S10318-cpt)"""

    COMP = "COMP"
    ARR = "ARR"
    DEP = "DEP"
    CTRLV = "CTRLV"


class ActRelationshipHasSupport(Enum):
    """specDomain: S10330 (C-0-T10317-S10329-S10330-cpt)"""

    SPRT = "SPRT"
    SPRTBND = "SPRTBND"


class ActRelationshipMitigates(Enum):
    """specDomain: S19986 (C-0-T10317-A18977-S10321-S19986-cpt)"""

    MITGT = "MITGT"
    RCVY = "RCVY"


class ActRelationshipOutcome(Enum):
    """specDomain: S10324 (C-0-T10317-S10324-cpt)"""

    OBJC = "OBJC"
    OBJF = "OBJF"
    OUTC = "OUTC"
    GOAL = "GOAL"
    RISK = "RISK"


class ActRelationshipPertainsValue(Enum):
    PERT = "PERT"
    NAME = "NAME"
    AUTH = "AUTH"
    COVBY = "COVBY"
    ELNK = "ELNK"
    EXPL = "EXPL"
    PREV = "PREV"
    REFV = "REFV"
    SUBJ = "SUBJ"
    DRIV = "DRIV"
    CAUS = "CAUS"
    MFST = "MFST"
    ITEMSLOC = "ITEMSLOC"
    LIMIT = "LIMIT"
    EVID = "EVID"
    REFR = "REFR"
    SUMM = "SUMM"


class ActRelationshipPosting(Enum):
    """abstDomain: A19609 (C-0-T10317-S10329-A14900-A19609-cpt)"""

    CREDIT = "CREDIT"
    DEBIT = "DEBIT"


class ActRelationshipReason(Enum):
    """specDomain: S10321 (C-0-T10317-A18977-S10321-cpt)"""

    MITGT = "MITGT"
    RCVY = "RCVY"
    RSON = "RSON"
    BLOCK = "BLOCK"
    CURE_ADJ = "CURE.ADJ"
    MTGT_ADJ = "MTGT.ADJ"
    CURE = "CURE"
    DIAG = "DIAG"
    SYMP = "SYMP"


class ActRelationshipSequel(Enum):
    """specDomain: S10337 (C-0-T10317-S10337-cpt)"""

    XCRPT = "XCRPT"
    VRXCRPT = "VRXCRPT"
    FLFS = "FLFS"
    OCCR = "OCCR"
    OREF = "OREF"
    SCH = "SCH"
    SEQL = "SEQL"
    DOC = "DOC"
    GEVL = "GEVL"
    GEN = "GEN"
    OPTN = "OPTN"
    INST = "INST"
    APND = "APND"
    MTCH = "MTCH"
    MOD = "MOD"
    RCHAL = "RCHAL"
    RPLC = "RPLC"
    REV = "REV"
    SUCC = "SUCC"
    XFRM = "XFRM"
    UPDT = "UPDT"


class ActRelationshipTemporallyPertains(Enum):
    """abstDomain: A19587 (C-0-T10317-S10329-A19587-cpt)"""

    SAE = "SAE"
    SAS = "SAS"


class AddressPartType(Enum):
    """vocSet: T10642 (C-0-T10642-cpt)"""

    ADL = "ADL"
    UNIT = "UNIT"
    UNID = "UNID"
    DAL = "DAL"
    DINSTA = "DINSTA"
    DINSTQ = "DINSTQ"
    DINST = "DINST"
    DMOD = "DMOD"
    DMODID = "DMODID"
    BNS = "BNS"
    POB = "POB"
    BNR = "BNR"
    BNN = "BNN"
    STR = "STR"
    STB = "STB"
    STTYP = "STTYP"
    SAL = "SAL"
    DIR = "DIR"
    CAR = "CAR"
    CEN = "CEN"
    CNT = "CNT"
    CPA = "CPA"
    DEL = "DEL"
    CTY = "CTY"
    ZIP = "ZIP"
    PRE = "PRE"
    STA = "STA"


class CalendarCycleOneLetter(Enum):
    """abstDomain: A10701 (C-0-T10684-A10701-cpt)"""

    D = "D"
    J = "J"
    H = "H"
    N = "N"
    M = "M"
    S = "S"
    W = "W"
    Y = "Y"


class CalendarCycleTwoLetterValue(Enum):
    CD = "CD"
    DM = "DM"
    DW = "DW"
    DY = "DY"
    CH = "CH"
    HD = "HD"
    CN = "CN"
    NH = "NH"
    CM = "CM"
    MY = "MY"
    CS = "CS"
    SN = "SN"
    CW = "CW"
    WY = "WY"
    CY = "CY"


class CommunicationFunctionType(Enum):
    """vocSet: T16031 (C-0-T16031-cpt)"""

    RCV = "RCV"
    RSP = "RSP"
    SND = "SND"


class CompressionAlgorithm(Enum):
    """vocSet: T10620 (C-0-T10620-cpt)"""

    Z = "Z"
    DF = "DF"
    GZ = "GZ"
    ZL = "ZL"


class ContextControl(Enum):
    """vocSet: T16478 (C-0-T16478-cpt)"""

    AN = "AN"
    AP = "AP"
    ON = "ON"
    OP = "OP"


class EntityClass(Enum):
    """vocSet: T10882 (C-0-T10882-cpt)"""

    NLIV = "NLIV"
    ANM = "ANM"
    MIC = "MIC"
    PLNT = "PLNT"
    LIV = "LIV"
    PSN = "PSN"
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"
    MAT = "MAT"
    CHEM = "CHEM"
    FOOD = "FOOD"
    STATE = "STATE"
    NAT = "NAT"
    ORG = "ORG"
    PUB = "PUB"
    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"
    ENT = "ENT"
    RGRP = "RGRP"
    HCE = "HCE"


class EntityClassContainer(Enum):
    """specDomain: S11622 (C-0-T10882-S13922-S10883-S13934-S11622-cpt)"""

    CONT = "CONT"
    HOLD = "HOLD"


class EntityClassDevice(Enum):
    """specDomain: S11623 (C-0-T10882-S13922-S10883-S13934-S11623-cpt)"""

    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"


class EntityClassManufacturedMaterial(Enum):
    """specDomain: S13934 (C-0-T10882-S13922-S10883-S13934-cpt)"""

    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"


class EntityClassMaterial(Enum):
    """specDomain: S10883 (C-0-T10882-S13922-S10883-cpt)"""

    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"
    MAT = "MAT"
    CHEM = "CHEM"
    FOOD = "FOOD"


class EntityClassNonPersonLivingSubject(Enum):
    """specDomain: S11621 (C-0-T10882-S13922-S10884-S11621-cpt)"""

    NLIV = "NLIV"
    ANM = "ANM"
    MIC = "MIC"
    PLNT = "PLNT"


class EntityClassOrganization(Enum):
    """specDomain: S10889 (C-0-T10882-S13922-S10889-cpt)"""

    STATE = "STATE"
    NAT = "NAT"
    ORG = "ORG"
    PUB = "PUB"


class EntityClassPlace(Enum):
    """specDomain: S10892 (C-0-T10882-S13922-S10892-cpt)"""

    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"


class EntityClassRoot(Enum):
    """specDomain: S13922 (C-0-T10882-S13922-cpt)"""

    NLIV = "NLIV"
    ANM = "ANM"
    MIC = "MIC"
    PLNT = "PLNT"
    LIV = "LIV"
    PSN = "PSN"
    CONT = "CONT"
    HOLD = "HOLD"
    DEV = "DEV"
    CER = "CER"
    MODDV = "MODDV"
    MMAT = "MMAT"
    MAT = "MAT"
    CHEM = "CHEM"
    FOOD = "FOOD"
    STATE = "STATE"
    NAT = "NAT"
    ORG = "ORG"
    PUB = "PUB"
    PLC = "PLC"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    COUNTY = "COUNTY"
    PROVINCE = "PROVINCE"
    ENT = "ENT"
    RGRP = "RGRP"
    HCE = "HCE"


class EntityClassState(Enum):
    """specDomain: S10890 (C-0-T10882-S13922-S10889-S10890-cpt)"""

    STATE = "STATE"
    NAT = "NAT"


class EntityDeterminer(Enum):
    """vocSet: T10878 (C-0-T10878-cpt)"""

    KIND = "KIND"
    QUANTIFIED_KIND = "QUANTIFIED_KIND"
    INSTANCE = "INSTANCE"


class EntityDeterminerDetermined(Enum):
    """specDomain: S10879 (C-0-T10878-S10879-cpt)"""

    KIND = "KIND"
    QUANTIFIED_KIND = "QUANTIFIED_KIND"


class EntityNamePartQualifier(Enum):
    """vocSet: T15888 (C-0-T15888-cpt)"""

    LS = "LS"
    AC = "AC"
    NB = "NB"
    PR = "PR"
    VV = "VV"
    AD = "AD"
    BR = "BR"
    SP = "SP"
    CL = "CL"
    IN = "IN"
    TITLE = "TITLE"


class EntityNamePartType(Enum):
    """vocSet: T15880 (C-0-T15880-cpt)"""

    DEL = "DEL"
    PFX = "PFX"
    SFX = "SFX"
    FAM = "FAM"
    GIV = "GIV"


class EntityNameUse(Enum):
    """vocSet: T15913 (C-0-T15913-cpt)"""

    SRCH = "SRCH"
    SNDX = "SNDX"
    PHON = "PHON"
    L = "L"
    OR = "OR"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    C = "C"
    P = "P"
    A = "A"
    I = "I"
    R = "R"
    ASGN = "ASGN"


class IntegrityCheckAlgorithm(Enum):
    """vocSet: T17385 (C-0-T17385-cpt)"""

    SHA_1 = "SHA-1"
    SHA_256 = "SHA-256"


class NullFlavor(Enum):
    """vocSet: T10609 (C-0-T10609-cpt)"""

    OTH = "OTH"
    NINF = "NINF"
    PINF = "PINF"
    ASKU = "ASKU"
    NAV = "NAV"
    UNK = "UNK"
    QS = "QS"
    NASK = "NASK"
    TRC = "TRC"
    NI = "NI"
    MSK = "MSK"
    NA = "NA"
    UNC = "UNC"


class ParticipationInformationRecipient(Enum):
    """specDomain: S10263 (C-0-T10901-S21573-S10263-cpt)"""

    IRCP = "IRCP"
    REFB = "REFB"
    REFT = "REFT"
    PRCP = "PRCP"
    TRC = "TRC"
    NOT = "NOT"


class ParticipationParticipation(Enum):
    """specDomain: S21573 (C-0-T10901-S21573-cpt)"""

    ADM = "ADM"
    ATND = "ATND"
    CALLBCK = "CALLBCK"
    CON = "CON"
    DIS = "DIS"
    ESC = "ESC"
    REF = "REF"
    IND = "IND"
    BEN = "BEN"
    CAGNT = "CAGNT"
    COV = "COV"
    GUAR = "GUAR"
    HLD = "HLD"
    RCV = "RCV"
    RCT = "RCT"
    TRANS = "TRANS"
    ENT = "ENT"
    AUT = "AUT"
    INF = "INF"
    WIT = "WIT"
    IRCP = "IRCP"
    REFB = "REFB"
    REFT = "REFT"
    PRCP = "PRCP"
    TRC = "TRC"
    NOT = "NOT"
    PRF = "PRF"
    DIST = "DIST"
    PPRF = "PPRF"
    SPRF = "SPRF"
    EXPART = "EXPART"
    EXSRC = "EXSRC"
    EXPTRGT = "EXPTRGT"
    DEV = "DEV"
    NRD = "NRD"
    RDV = "RDV"
    SBJ = "SBJ"
    SPC = "SPC"
    DIR = "DIR"
    EXPAGNT = "EXPAGNT"
    BBY = "BBY"
    CSM = "CSM"
    DON = "DON"
    PRD = "PRD"
    LOC = "LOC"
    DST = "DST"
    ELOC = "ELOC"
    ORG = "ORG"
    RML = "RML"
    VIA = "VIA"
    VRF = "VRF"
    AUTHEN = "AUTHEN"
    LA = "LA"
    PART = "PART"
    CST = "CST"
    RESP = "RESP"


class ParticipationPhysicalPerformer(Enum):
    """specDomain: S10248 (C-0-T10901-S21573-S10248-cpt)"""

    PRF = "PRF"
    DIST = "DIST"
    PPRF = "PPRF"
    SPRF = "SPRF"


class ParticipationTargetDevice(Enum):
    """specDomain: S10298 (C-0-T10901-S21573-S10286-S10298-cpt)"""

    DEV = "DEV"
    NRD = "NRD"
    RDV = "RDV"


class ParticipationTargetLocation(Enum):
    """specDomain: S10302 (C-0-T10901-S21573-S10302-cpt)"""

    LOC = "LOC"
    DST = "DST"
    ELOC = "ELOC"
    ORG = "ORG"
    RML = "RML"
    VIA = "VIA"


class ParticipationTargetSubject(Enum):
    """specDomain: S10287 (C-0-T10901-S21573-S10286-S10287-cpt)"""

    SBJ = "SBJ"
    SPC = "SPC"


class ParticipationType(Enum):
    """vocSet: T10901 (C-0-T10901-cpt)"""

    ADM = "ADM"
    ATND = "ATND"
    CALLBCK = "CALLBCK"
    CON = "CON"
    DIS = "DIS"
    ESC = "ESC"
    REF = "REF"
    IND = "IND"
    BEN = "BEN"
    CAGNT = "CAGNT"
    COV = "COV"
    GUAR = "GUAR"
    HLD = "HLD"
    RCV = "RCV"
    RCT = "RCT"
    TRANS = "TRANS"
    ENT = "ENT"
    AUT = "AUT"
    INF = "INF"
    WIT = "WIT"
    IRCP = "IRCP"
    REFB = "REFB"
    REFT = "REFT"
    PRCP = "PRCP"
    TRC = "TRC"
    NOT = "NOT"
    PRF = "PRF"
    DIST = "DIST"
    PPRF = "PPRF"
    SPRF = "SPRF"
    EXPART = "EXPART"
    EXSRC = "EXSRC"
    EXPTRGT = "EXPTRGT"
    DEV = "DEV"
    NRD = "NRD"
    RDV = "RDV"
    SBJ = "SBJ"
    SPC = "SPC"
    DIR = "DIR"
    EXPAGNT = "EXPAGNT"
    BBY = "BBY"
    CSM = "CSM"
    DON = "DON"
    PRD = "PRD"
    LOC = "LOC"
    DST = "DST"
    ELOC = "ELOC"
    ORG = "ORG"
    RML = "RML"
    VIA = "VIA"
    VRF = "VRF"
    AUTHEN = "AUTHEN"
    LA = "LA"
    PART = "PART"
    CST = "CST"
    RESP = "RESP"


class ParticipationVerifier(Enum):
    """specDomain: S10259 (C-0-T10901-S21573-S10259-cpt)"""

    VRF = "VRF"
    AUTHEN = "AUTHEN"
    LA = "LA"


class PostalAddressUse(Enum):
    """vocSet: T10637 (C-0-T10637-cpt)"""

    H = "H"
    HP = "HP"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    TMP = "TMP"
    ABC = "ABC"
    IDE = "IDE"
    SYL = "SYL"
    PHYS = "PHYS"
    PST = "PST"


class ProbabilityDistributionType(Enum):
    """vocSet: T10747 (C-0-T10747-cpt)"""

    G = "G"
    F = "F"
    T = "T"
    B = "B"
    X2 = "X2"
    E = "E"
    LN = "LN"
    N = "N"
    U = "U"


class RoleClassAgent(Enum):
    """specDomain: S14006 (C-0-T11555-S13940-A19313-A19316-A10416-S14006-cpt)"""

    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"
    AGNT = "AGNT"
    GUARD = "GUARD"


class RoleClassAssignedEntity(Enum):
    """specDomain: S11595 (C-0-T11555-S13940-A19313-A19316-A10416-S14006-S11595-cpt)"""

    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"


class RoleClassContact(Enum):
    """specDomain: S12205 (C-0-T11555-S13940-A19313-A19316-A10416-S14006-S11595-S12205-cpt)"""

    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"


class RoleClassCoveredParty(Enum):
    """specDomain: S14011 (C-0-T11555-S13940-A19313-A19316-A10416-S14011-cpt)"""

    NAMED = "NAMED"
    DEPEN = "DEPEN"
    INDIV = "INDIV"
    SUBSCR = "SUBSCR"
    COVPTY = "COVPTY"
    CLAIM = "CLAIM"
    PROG = "PROG"


class RoleClassDistributedMaterial(Enum):
    """specDomain: S10418 (C-0-T11555-S13940-A19313-A19105-S10418-cpt)"""

    DST = "DST"
    RET = "RET"


class RoleClassEmployee(Enum):
    """specDomain: S11569 (C-0-T11555-S13940-A19313-A19316-A10416-S11569-cpt)"""

    EMP = "EMP"
    MIL = "MIL"


class RoleClassIngredientEntity(Enum):
    """specDomain: S10430 (C-0-T11555-S13940-A10429-S10430-cpt)"""

    IACT = "IACT"
    COLR = "COLR"
    FLVR = "FLVR"
    PRSV = "PRSV"
    STBL = "STBL"
    ACTI = "ACTI"
    ACTIB = "ACTIB"
    ACTIM = "ACTIM"
    ACTIR = "ACTIR"
    INGR = "INGR"
    ADTV = "ADTV"
    BASE = "BASE"


class RoleClassIsSpeciesEntity(Enum):
    """specDomain: S10441 (C-0-T11555-S13940-A10428-S10441-cpt)"""

    GEN = "GEN"
    GRIC = "GRIC"


class RoleClassLicensedEntity(Enum):
    """specDomain: S16773 (C-0-T11555-S13940-A19313-A19316-A10416-S16773-cpt)"""

    LIC = "LIC"
    PROV = "PROV"
    NOT = "NOT"


class RoleClassLocatedEntity(Enum):
    """specDomain: S16815 (C-0-T11555-S13940-A10429-S16815-cpt)"""

    LOCE = "LOCE"
    STOR = "STOR"


class RoleClassManufacturedProduct(Enum):
    """specDomain: S11580 (C-0-T11555-S13940-A19313-A19105-S11580-cpt)"""

    MANU = "MANU"
    THER = "THER"


class RoleClassMutualRelationship(Enum):
    """abstDomain: A19316 (C-0-T11555-S13940-A19313-A19316-cpt)"""

    CON = "CON"
    ECON = "ECON"
    NOK = "NOK"
    ASSIGNED = "ASSIGNED"
    COMPAR = "COMPAR"
    SGNOFF = "SGNOFF"
    AGNT = "AGNT"
    GUARD = "GUARD"
    NAMED = "NAMED"
    DEPEN = "DEPEN"
    INDIV = "INDIV"
    SUBSCR = "SUBSCR"
    COVPTY = "COVPTY"
    CLAIM = "CLAIM"
    PROG = "PROG"
    EMP = "EMP"
    MIL = "MIL"
    INVSBJ = "INVSBJ"
    CASEBJ = "CASEBJ"
    RESBJ = "RESBJ"
    LIC = "LIC"
    PROV = "PROV"
    NOT = "NOT"
    AFFL = "AFFL"
    CIT = "CIT"
    CRINV = "CRINV"
    CRSPNSR = "CRSPNSR"
    SPNSR = "SPNSR"
    GUAR = "GUAR"
    PAYOR = "PAYOR"
    PAT = "PAT"
    PAYEE = "PAYEE"
    POLHOLD = "POLHOLD"
    QUAL = "QUAL"
    STD = "STD"
    UNDWRT = "UNDWRT"
    CAREGIVER = "CAREGIVER"
    PRS = "PRS"


class RoleClassOntological(Enum):
    """abstDomain: A10428 (C-0-T11555-S13940-A10428-cpt)"""

    GEN = "GEN"
    GRIC = "GRIC"
    EQUIV = "EQUIV"
    SAME = "SAME"
    SUBY = "SUBY"
    INST = "INST"
    SUBS = "SUBS"


class RoleClassPartitive(Enum):
    """abstDomain: A10429 (C-0-T11555-S13940-A10429-cpt)"""

    EXPAGTCAR = "EXPAGTCAR"
    EXPVECTOR = "EXPVECTOR"
    FOMITE = "FOMITE"
    IACT = "IACT"
    COLR = "COLR"
    FLVR = "FLVR"
    PRSV = "PRSV"
    STBL = "STBL"
    ACTI = "ACTI"
    ACTIB = "ACTIB"
    ACTIM = "ACTIM"
    ACTIR = "ACTIR"
    INGR = "INGR"
    ADTV = "ADTV"
    BASE = "BASE"
    LOCE = "LOCE"
    STOR = "STOR"
    PART = "PART"
    ACTM = "ACTM"
    SPEC = "SPEC"
    ALQT = "ALQT"
    ISLT = "ISLT"
    CONT = "CONT"
    MBR = "MBR"


class RoleClassPartitivePartByBot(Enum):
    """specDomain: S19102 (C-0-T11555-S13940-A10429-S19102-cpt)"""

    PART = "PART"
    ACTM = "ACTM"


class RoleClassPassive(Enum):
    """abstDomain: A19105 (C-0-T11555-S13940-A19313-A19105-cpt)"""

    DST = "DST"
    RET = "RET"
    MANU = "MANU"
    THER = "THER"
    SDLOC = "SDLOC"
    DSDLOC = "DSDLOC"
    ISDLOC = "ISDLOC"
    ADMM = "ADMM"
    ACCESS = "ACCESS"
    BIRTHPL = "BIRTHPL"
    EXPR = "EXPR"
    HLTHCHRT = "HLTHCHRT"
    HLD = "HLD"
    IDENT = "IDENT"
    MNT = "MNT"
    OWN = "OWN"
    DEATHPLC = "DEATHPLC"
    RGPR = "RGPR"
    TERR = "TERR"
    WRTE = "WRTE"


class RoleClassRootValue(Enum):
    ROL = "ROL"


class RoleClassServiceDeliveryLocation(Enum):
    """specDomain: S16927 (C-0-T11555-S13940-A19313-A19105-S16927-cpt)"""

    SDLOC = "SDLOC"
    DSDLOC = "DSDLOC"
    ISDLOC = "ISDLOC"


class RoleClassSpecimen(Enum):
    """specDomain: S11591 (C-0-T11555-S13940-A10429-S11591-cpt)"""

    SPEC = "SPEC"
    ALQT = "ALQT"
    ISLT = "ISLT"


class RoleLinkType(Enum):
    """vocSet: T11603 (C-0-T11603-cpt)"""

    REL = "REL"
    IDENT = "IDENT"
    DIRAUTH = "DIRAUTH"
    INDAUTH = "INDAUTH"
    PART = "PART"
    BACKUP = "BACKUP"
    REPL = "REPL"


class SetOperator(Enum):
    """vocSet: T17416 (C-0-T17416-cpt)"""

    VALUE_SET_OPERATOR = "_ValueSetOperator"
    H = "H"
    E = "E"
    I = "I"
    A = "A"
    P = "P"


class TelecommunicationAddressUse(Enum):
    """vocSet: T201 (C-0-T201-cpt)"""

    H = "H"
    HP = "HP"
    HV = "HV"
    WP = "WP"
    DIR = "DIR"
    PUB = "PUB"
    BAD = "BAD"
    TMP = "TMP"
    AS = "AS"
    EC = "EC"
    MC = "MC"
    PG = "PG"


class TimingEvent(Enum):
    """vocSet: T10706 (C-0-T10706-cpt)"""

    AC = "AC"
    ACD = "ACD"
    ACM = "ACM"
    ACV = "ACV"
    HS = "HS"
    IC = "IC"
    ICD = "ICD"
    ICM = "ICM"
    ICV = "ICV"
    PC = "PC"
    PCD = "PCD"
    PCM = "PCM"
    PCV = "PCV"


class XAccommodationRequestorRole(Enum):
    """abstDomain: A19352 (C-0-T11555-A19352-cpt)"""

    AGNT = "AGNT"
    PROV = "PROV"
    PAT = "PAT"
    PRS = "PRS"


class XActClassDocumentEntryAct(Enum):
    """abstDomain: A19599 (C-0-T11527-A19599-cpt)"""

    ACCM = "ACCM"
    ACT = "ACT"
    PCPR = "PCPR"
    CTTEVENT = "CTTEVENT"
    CONS = "CONS"
    INC = "INC"
    INFRM = "INFRM"
    REG = "REG"
    SPCTRT = "SPCTRT"
    TRNS = "TRNS"


class XActClassDocumentEntryOrganizer(Enum):
    """abstDomain: A19598 (C-0-T11527-A19598-cpt)"""

    CLUSTER = "CLUSTER"
    BATTERY = "BATTERY"


class XActMoodDefEvn(Enum):
    """abstDomain: A19375 (C-0-T10196-A19375-cpt)"""

    DEF = "DEF"
    EVN = "EVN"


class XActMoodDocumentObservation(Enum):
    """abstDomain: A18943 (C-0-T10196-A18943-cpt)"""

    GOL = "GOL"
    DEF = "DEF"
    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XActMoodIntentEvent(Enum):
    """abstDomain: A16742 (C-0-T10196-A16742-cpt)"""

    EVN = "EVN"


class XActMoodOrdPrms(Enum):
    """abstDomain: A16735 (C-0-T10196-A16735-cpt)"""

    PRMS = "PRMS"
    RQO = "RQO"


class XActRelationshipDocument(Enum):
    """abstDomain: A11610 (C-0-T10317-A11610-cpt)"""

    APND = "APND"
    RPLC = "RPLC"
    XFRM = "XFRM"


class XActRelationshipEntry(Enum):
    """abstDomain: A19446 (C-0-T10317-A19446-cpt)"""

    COMP = "COMP"
    DRIV = "DRIV"


class XActRelationshipEntryRelationship(Enum):
    """abstDomain: A19447 (C-0-T10317-A19447-cpt)"""

    XCRPT = "XCRPT"
    GEVL = "GEVL"
    COMP = "COMP"
    RSON = "RSON"
    SUBJ = "SUBJ"
    SPRT = "SPRT"
    CAUS = "CAUS"
    MFST = "MFST"
    REFR = "REFR"
    SAS = "SAS"


class XActRelationshipExternalReference(Enum):
    """abstDomain: A19000 (C-0-T10317-A19000-cpt)"""

    XCRPT = "XCRPT"
    ELNK = "ELNK"
    SUBJ = "SUBJ"
    SPRT = "SPRT"
    REFR = "REFR"
    RPLC = "RPLC"


class XActRelationshipPatientTransport(Enum):
    """abstDomain: A19005 (C-0-T10317-A19005-cpt)"""

    ARR = "ARR"
    DEP = "DEP"


class XActRelationshipPertinentInfo(Enum):
    """abstDomain: A19562 (C-0-T10317-A19562-cpt)"""

    SUBJ = "SUBJ"
    SPRT = "SPRT"
    CAUS = "CAUS"
    MFST = "MFST"
    REFR = "REFR"


class XActRelationshipRelatedAuthorizations(Enum):
    """abstDomain: A19825 (C-0-T10317-A19825-cpt)"""

    AUTH = "AUTH"
    REFR = "REFR"


class XActReplaceOrRevise(Enum):
    """abstDomain: A19764 (C-0-T10317-A19764-cpt)"""

    MOD = "MOD"
    RPLC = "RPLC"


class XClinicalStatementActMood(Enum):
    """abstDomain: A19649 (C-0-T10196-A19649-cpt)"""

    APT = "APT"
    ARQ = "ARQ"
    DEF = "DEF"
    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementEncounterMood(Enum):
    """abstDomain: A19648 (C-0-T10196-A19648-cpt)"""

    APT = "APT"
    ARQ = "ARQ"
    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementObservationMood(Enum):
    """abstDomain: A19644 (C-0-T10196-A19644-cpt)"""

    GOL = "GOL"
    APT = "APT"
    ARQ = "ARQ"
    DEF = "DEF"
    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementProcedureMood(Enum):
    """abstDomain: A19647 (C-0-T10196-A19647-cpt)"""

    APT = "APT"
    ARQ = "ARQ"
    DEF = "DEF"
    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementSubstanceMood(Enum):
    """abstDomain: A19645 (C-0-T10196-A19645-cpt)"""

    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XClinicalStatementSupplyMood(Enum):
    """abstDomain: A19646 (C-0-T10196-A19646-cpt)"""

    EVN = "EVN"
    INT = "INT"


class XDeterminerInstanceKind(Enum):
    """abstDomain: A19670 (C-0-T10878-A19670-cpt)"""

    KIND = "KIND"
    QUANTIFIED_KIND = "QUANTIFIED_KIND"
    INSTANCE = "INSTANCE"


class XDocumentActMood(Enum):
    """abstDomain: A19458 (C-0-T10196-A19458-cpt)"""

    APT = "APT"
    ARQ = "ARQ"
    DEF = "DEF"
    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XDocumentEncounterMood(Enum):
    """abstDomain: A19459 (C-0-T10196-A19459-cpt)"""

    APT = "APT"
    ARQ = "ARQ"
    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XDocumentEntrySubject(Enum):
    """abstDomain: A19367 (C-0-T11555-A19367-cpt)"""

    PAT = "PAT"
    PRS = "PRS"
    SPEC = "SPEC"


class XDocumentProcedureMood(Enum):
    """abstDomain: A19460 (C-0-T10196-A19460-cpt)"""

    APT = "APT"
    ARQ = "ARQ"
    DEF = "DEF"
    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XDocumentSubject(Enum):
    """abstDomain: A19368 (C-0-T11555-A19368-cpt)"""

    PAT = "PAT"
    PRS = "PRS"


class XDocumentSubstanceMood(Enum):
    """abstDomain: A19461 (C-0-T10196-A19461-cpt)"""

    EVN = "EVN"
    INT = "INT"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"


class XEncounterParticipant(Enum):
    """abstDomain: A19600 (C-0-T10901-A19600-cpt)"""

    ADM = "ADM"
    ATND = "ATND"
    CON = "CON"
    DIS = "DIS"
    REF = "REF"


class XInformationRecipient(Enum):
    """abstDomain: A19366 (C-0-T10901-A19366-cpt)"""

    PRCP = "PRCP"
    TRC = "TRC"


class XInformationRecipientRole(Enum):
    """abstDomain: A16772 (C-0-T11555-A16772-cpt)"""

    ASSIGNED = "ASSIGNED"
    HLTHCHRT = "HLTHCHRT"


class XLabProcessClassCodes(Enum):
    """abstDomain: A19657 (C-0-T11527-A19657-cpt)"""

    ACSN = "ACSN"
    CONTREG = "CONTREG"
    PROC = "PROC"
    SPCTRT = "SPCTRT"
    TRNS = "TRNS"


class XParticipationAuthorPerformer(Enum):
    """abstDomain: A19080 (C-0-T10901-A19080-cpt)"""

    AUT = "AUT"
    PRF = "PRF"


class XParticipationVrfRespSprfWit(Enum):
    """abstDomain: A19083 (C-0-T10901-A19083-cpt)"""

    RESP = "RESP"
    SPRF = "SPRF"
    VRF = "VRF"
    WIT = "WIT"


class XRoleClassAccommodationRequestor(Enum):
    """abstDomain: A19382 (C-0-T11555-A19382-cpt)"""

    AGNT = "AGNT"
    PROV = "PROV"
    PAT = "PAT"
    PRS = "PRS"


class XRoleClassCoverage(Enum):
    """abstDomain: A14008 (C-0-T11555-A14008-cpt)"""

    SPNSR = "SPNSR"
    COVPTY = "COVPTY"
    POLHOLD = "POLHOLD"
    UNDWRT = "UNDWRT"


class XRoleClassCoverageInvoice(Enum):
    """abstDomain: A14013 (C-0-T11555-A14013-cpt)"""

    PAYOR = "PAYOR"
    PAYEE = "PAYEE"


class XRoleClassCredentialedEntity(Enum):
    """abstDomain: A16930 (C-0-T11555-A16930-cpt)"""

    ASSIGNED = "ASSIGNED"
    QUAL = "QUAL"


class XRoleClassPayeePolicyRelationship(Enum):
    """abstDomain: A19395 (C-0-T11555-A19395-cpt)"""

    COVPTY = "COVPTY"
    GUAR = "GUAR"
    PROV = "PROV"
    PRS = "PRS"
    POLHOLD = "POLHOLD"


class XSuccReplPrev(Enum):
    """abstDomain: A19753 (C-0-T10317-A19753-cpt)"""

    PREV = "PREV"
    RPLC = "RPLC"
    SUCC = "SUCC"


class XServiceEventPerformer(Enum):
    """abstDomain: A19601 (C-0-T10901-A19601-cpt)"""

    PRF = "PRF"
    SPRF = "SPRF"
