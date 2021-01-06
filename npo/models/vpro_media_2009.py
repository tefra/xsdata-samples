from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
from npo.models.vpro_shared_2009 import (
    Image,
    OwnerTypeEnum,
    WorkflowEnumType,
)

__NAMESPACE__ = "urn:vpro:media:2009"


class AgeRatingType(Enum):
    VALUE_6 = "6"
    VALUE_9 = "9"
    VALUE_12 = "12"
    VALUE_14 = "14"
    VALUE_16 = "16"
    VALUE_18 = "18"
    ALL = "ALL"
    NOT_YET_RATED = "NOT_YET_RATED"


AgeRatingType.VALUE_6.__doc__ = "Suitable for people of age 6 and up."
AgeRatingType.VALUE_9.__doc__ = "Suitable for people of age 9 and up."
AgeRatingType.VALUE_12.__doc__ = "Suitable for people of age 12 and up."
AgeRatingType.VALUE_14.__doc__ = "Suitable for people of age 12 and up."
AgeRatingType.VALUE_16.__doc__ = "Suitable for people of age 16 and up."
AgeRatingType.VALUE_18.__doc__ = "Suitable for people of age 18 and up."
AgeRatingType.ALL.__doc__ = "Suitable for people of all ages."
AgeRatingType.NOT_YET_RATED.__doc__ = "Not yet rated"


class AspectRatioEnum(Enum):
    VALUE_4_3 = "4:3"
    VALUE_16_9 = "16:9"


@dataclass
class AudioAttributesType:
    class Meta:
        name = "audioAttributesType"

    number_of_channels: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfChannels",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    audio_coding: Optional[str] = field(
        default=None,
        metadata={
            "name": "audioCoding",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


class AvFileFormatEnum(Enum):
    MP3 = "MP3"
    RA = "RA"
    RM = "RM"
    MP4 = "MP4"
    WVC1 = "WVC1"
    WM = "WM"
    RAM = "RAM"
    WMP = "WMP"
    HTML = "HTML"
    M4_A = "M4A"
    M4_V = "M4V"
    DGPP = "DGPP"
    FLV = "FLV"
    HASP = "HASP"
    MPEG2 = "MPEG2"
    H264 = "H264"
    UNKNOWN = "UNKNOWN"


class AvTypeEnum(Enum):
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    MIXED = "MIXED"


@dataclass
class AvailableSubtitleType:
    class Meta:
        name = "availableSubtitleType"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class ChannelEnum(Enum):
    NED1 = "NED1"
    NED2 = "NED2"
    NED3 = "NED3"
    NEDE = "NEDE"
    RTL4 = "RTL4"
    RTL5 = "RTL5"
    SBS6 = "SBS6"
    RTL7 = "RTL7"
    VERO = "VERO"
    NET5 = "NET5"
    RTL8 = "RTL8"
    REGI = "REGI"
    OFRY = "OFRY"
    NOOR = "NOOR"
    RTVD = "RTVD"
    OOST = "OOST"
    GELD = "GELD"
    FLEV = "FLEV"
    BRAB = "BRAB"
    REGU = "REGU"
    NORH = "NORH"
    WEST = "WEST"
    RIJN = "RIJN"
    L1_TV = "L1TV"
    OZEE = "OZEE"
    AT5 = "AT5_"
    RNN7 = "RNN7"
    BVNT = "BVNT"
    EEN = "EEN_"
    KETN = "KETN"
    VTM = "VTM_"
    KA2 = "KA2_"
    VT4 = "VT4_"
    LUNE = "LUNE"
    LDUE = "LDUE"
    RTBF = "RTBF"
    ARD = "ARD_"
    ZDF = "ZDF_"
    WDR = "WDR_"
    N_3 = "N_3_"
    SUDW = "SUDW"
    SWF = "SWF_"
    RTL = "RTL_"
    SAT1 = "SAT1"
    PRO7 = "PRO7"
    VALUE_3_SAT = "3SAT"
    KABE = "KABE"
    ARTE = "ARTE"
    T5_ME = "T5ME"
    FRA2 = "FRA2"
    FRA3 = "FRA3"
    BBC1 = "BBC1"
    BBC2 = "BBC2"
    BBTH = "BBTH"
    BBTC = "BBTC"
    BBCF = "BBCF"
    BBFC = "BBFC"
    BBCP = "BBCP"
    TRTI = "TRTI"
    SHOW = "SHOW"
    LIGT = "LIGT"
    TURK = "TURK"
    ATVT = "ATVT"
    FOXT = "FOXT"
    HABN = "HABN"
    STTV = "STTV"
    RRTM = "RRTM"
    RMBC = "RMBC"
    RART = "RART"
    ARTM = "ARTM"
    TVBS = "TVBS"
    ASIA = "ASIA"
    TIVI = "TIVI"
    B4_UM = "B4UM"
    PCNE = "PCNE"
    PATN = "PATN"
    ZEET = "ZEET"
    ZEEC = "ZEEC"
    TVE = "TVE_"
    RAI = "RAI_"
    RAID = "RAID"
    RAIT = "RAIT"
    TEVE = "TEVE"
    ERTS = "ERTS"
    STV = "STV_"
    NTV = "NTV_"
    TVPO = "TVPO"
    NOSJ = "NOSJ"
    CULT = "CULT"
    VALUE_101 = "101_"
    PO24 = "PO24"
    HILV = "HILV"
    HOLL = "HOLL"
    GESC = "GESC"
    VALUE_3_VCN = "3VCN"
    VALUE_3_VOS = "3VOS"
    STER = "STER"
    NCRV = "NCRV"
    OPVO = "OPVO"
    CONS = "CONS"
    HUMO = "HUMO"
    ENTE = "ENTE"
    FASH = "FASH"
    COMC = "COMC"
    TBN = "TBN_"
    DISC = "DISC"
    ZONE = "ZONE"
    ANPL = "ANPL"
    CLUB = "CLUB"
    NAGE = "NAGE"
    TRAC = "TRAC"
    NGHD = "NGHD"
    WILD = "WILD"
    GARU = "GARU"
    ZAZA = "ZAZA"
    FAM7 = "FAM7"
    DTAL = "DTAL"
    SCIE = "SCIE"
    CIVI = "CIVI"
    DIHD = "DIHD"
    HIST = "HIST"
    TRAV = "TRAV"
    HETG = "HETG"
    GOED = "GOED"
    BABY = "BABY"
    DH1 = "DH1_"
    LITV = "LITV"
    LIVE = "LIVE"
    STAR = "STAR"
    WEER = "WEER"
    REAL = "REAL"
    SCIF = "SCIF"
    VALUE_13_ST = "13ST"
    CARC = "CARC"
    NOSN = "NOSN"
    HISH = "HISH"
    BRHD = "BRHD"
    FANT = "FANT"
    RACW = "RACW"
    COMF = "COMF"
    DIER = "DIER"
    POKE = "POKE"
    MNET = "MNET"
    VOOM = "VOOM"
    ZONH = "ZONH"
    KPN1 = "KPN1"
    KPN2 = "KPN2"
    KPN3 = "KPN3"
    KPN4 = "KPN4"
    ZIZO = "ZIZO"
    DVIC = "DVIC"
    DVB1 = "DVB1"
    DVB2 = "DVB2"
    DVB3 = "DVB3"
    NICK = "NICK"
    NIJN = "NIJN"
    NIKT = "NIKT"
    NIKH = "NIKH"
    CART = "CART"
    BOOM = "BOOM"
    CNN = "CNN_"
    BBCW = "BBCW"
    EURN = "EURN"
    SKNE = "SKNE"
    BLOO = "BLOO"
    CNBC = "CNBC"
    PALJ = "PALJ"
    ALJA = "ALJA"
    FOXN = "FOXN"
    FXNL = "FXNL"
    MTV = "MTV_"
    MTV2 = "MTV2"
    HITS = "HITS"
    BASE = "BASE"
    MTVB = "MTVB"
    TMF = "TMF_"
    TMFN = "TMFN"
    TMFP = "TMFP"
    TMFY = "TMFY"
    TVOR = "TVOR"
    VH1_E = "VH1E"
    VH1_C = "VH1C"
    PERC = "PERC"
    MEZZ = "MEZZ"
    EURO = "EURO"
    EUR2 = "EUR2"
    EXTR = "EXTR"
    MOTO = "MOTO"
    SAIL = "SAIL"
    ESPN = "ESPN"
    NASE = "NASE"
    SP11 = "SP11"
    SP12 = "SP12"
    SP13 = "SP13"
    SP14 = "SP14"
    SP15 = "SP15"
    SP16 = "SP16"
    SP17 = "SP17"
    SP18 = "SP18"
    S1_HD = "S1HD"
    FIL1 = "FIL1"
    FIL2 = "FIL2"
    FIL3 = "FIL3"
    FL11 = "FL11"
    FL1_P = "FL1P"
    FL12 = "FL12"
    FL13 = "FL13"
    FLHD = "FLHD"
    MGMM = "MGMM"
    TCM = "TCM_"
    HALL = "HALL"
    ACNW = "ACNW"
    RHUS = "RHUS"
    PLAY = "PLAY"
    ADUL = "ADUL"
    PSPI = "PSPI"
    HUST = "HUST"
    OXMO = "OXMO"
    XM24 = "XM24"
    OU24 = "OU24"
    RAD1 = "RAD1"
    RAD2 = "RAD2"
    R2_SJ = "R2SJ"
    RAD3 = "RAD3"
    R3_KX = "R3KX"
    RAD4 = "RAD4"
    R4_CO = "R4CO"
    RAD5 = "RAD5"
    R5_ST = "R5ST"
    RAD6 = "RAD6"
    REGR = "REGR"
    RFRY = "RFRY"
    RNOO = "RNOO"
    ROST = "ROST"
    RGEL = "RGEL"
    RFLE = "RFLE"
    RBRA = "RBRA"
    RUTR = "RUTR"
    RNOH = "RNOH"
    RWST = "RWST"
    RRIJ = "RRIJ"
    LRAD = "LRAD"
    RZEE = "RZEE"
    COMM = "COMM"
    RVER = "RVER"
    SLAM = "SLAM"
    SKYR = "SKYR"
    BNRN = "BNRN"
    KINK = "KINK"
    PCAZ = "PCAZ"
    QMUS = "QMUS"
    R538 = "R538"
    GOLD = "GOLD"
    ARRO = "ARRO"
    FUNX = "FUNX"
    FNXA = "FNXA"
    FNXR = "FNXR"
    FNXU = "FNXU"
    FNXD = "FNXD"
    FNXAR = "FNXAR"
    FNXDA = "FNXDA"
    FNXHH = "FNXHH"
    FNXLA = "FNXLA"
    FNXRE = "FNXRE"
    FNXSJ = "FNXSJ"
    CLAS = "CLAS"
    BEL1 = "BEL1"
    BEL2 = "BEL2"
    KLAR = "KLAR"
    BBR1 = "BBR1"
    BBR2 = "BBR2"
    BBR3 = "BBR3"
    BBR4 = "BBR4"
    BBWS = "BBWS"
    BBCX = "BBCX"
    NDR3 = "NDR3"
    WDR4 = "WDR4"
    WDR3 = "WDR3"
    ONL1 = "ONL1"
    OMEG = "OMEG"
    D24_K = "D24K"
    H1_NL = "H1NL"
    SYFY = "SYFY"
    SBS9 = "SBS9"
    DIXD = "DIXD"
    BRNL = "BRNL"
    FOXL = "FOXL"
    TLC = "TLC_"
    BCFS = "BCFS"
    AMC = "AMC_"
    FLM1 = "FLM1"
    ZGS1 = "ZGS1"
    BRTZ = "BRTZ"
    RTLF = "RTLF"
    TVDR = "TVDR"
    VRTC = "VRTC"
    XXXX = "XXXX"


ChannelEnum.NED1.__doc__ = "NPO 1."
ChannelEnum.NED2.__doc__ = "NPO 2."
ChannelEnum.NED3.__doc__ = "NPO 3 &amp; Z@pp."
ChannelEnum.NEDE.__doc__ = "Nederland-e."
ChannelEnum.RTL4.__doc__ = "RTL 4."
ChannelEnum.RTL5.__doc__ = "RTL 5."
ChannelEnum.SBS6.__doc__ = "SBS 6."
ChannelEnum.RTL7.__doc__ = "RTL 7."
ChannelEnum.VERO.__doc__ = "Veronica/Jetix."
ChannelEnum.NET5.__doc__ = "Net 5."
ChannelEnum.RTL8.__doc__ = "RTL 8."
ChannelEnum.REGI.__doc__ = "Regional TV combi-channel."
ChannelEnum.OFRY.__doc__ = "Omrop Fryslân tv."
ChannelEnum.NOOR.__doc__ = "TV Noord."
ChannelEnum.RTVD.__doc__ = "RTV Drenthe."
ChannelEnum.OOST.__doc__ = "TV Oost."
ChannelEnum.GELD.__doc__ = "TV Gelderland."
ChannelEnum.FLEV.__doc__ = "TV Flevoland."
ChannelEnum.BRAB.__doc__ = "Omroep Brabant."
ChannelEnum.REGU.__doc__ = "Regio TV Utrecht."
ChannelEnum.NORH.__doc__ = "TV Noord-Holland."
ChannelEnum.WEST.__doc__ = "TV West."
ChannelEnum.RIJN.__doc__ = "TV Rijnmond."
ChannelEnum.L1_TV.__doc__ = "L1 TV."
ChannelEnum.OZEE.__doc__ = "Omroep Zeeland."
ChannelEnum.AT5.__doc__ = "AT5."
ChannelEnum.RNN7.__doc__ = "RNN7."
ChannelEnum.BVNT.__doc__ = "BVN."
ChannelEnum.EEN.__doc__ = "Eén."
ChannelEnum.KETN.__doc__ = "Ketnet &amp; Canvas."
ChannelEnum.VTM.__doc__ = "VTM."
ChannelEnum.KA2.__doc__ = "2BE."
ChannelEnum.VT4.__doc__ = "VT4."
ChannelEnum.LUNE.__doc__ = "La Une (RTBF 1)."
ChannelEnum.LDUE.__doc__ = "La Deux (RTBF 2)."
ChannelEnum.RTBF.__doc__ = "RTBF Sat."
ChannelEnum.ARD.__doc__ = "ARD."
ChannelEnum.ZDF.__doc__ = "ZDF."
ChannelEnum.WDR.__doc__ = "WDR Fehrsehen"
ChannelEnum.N_3.__doc__ = "N3 (NDR)."
ChannelEnum.SUDW.__doc__ = "SWF Baden-Württemberg."
ChannelEnum.SWF.__doc__ = "SWF Rheinland-Pfalz."
ChannelEnum.RTL.__doc__ = "RTL Television."
ChannelEnum.SAT1.__doc__ = "Sat1."
ChannelEnum.PRO7.__doc__ = "Pro7."
ChannelEnum.VALUE_3_SAT.__doc__ = "3 Sat."
ChannelEnum.KABE.__doc__ = "Kabel 1."
ChannelEnum.ARTE.__doc__ = "ARTE."
ChannelEnum.T5_ME.__doc__ = "TV 5 Monde Europe."
ChannelEnum.FRA2.__doc__ = "France 2."
ChannelEnum.FRA3.__doc__ = "France 3."
ChannelEnum.BBC1.__doc__ = "BBC 1."
ChannelEnum.BBC2.__doc__ = "BBC 2."
ChannelEnum.BBTH.__doc__ = "BBC Three."
ChannelEnum.BBTC.__doc__ = "BBC Three / CBBC."
ChannelEnum.BBCF.__doc__ = "BBC Four."
ChannelEnum.BBFC.__doc__ = "BBC Four / Ceebies."
ChannelEnum.BBCP.__doc__ = "BBC Prime."
ChannelEnum.TRTI.__doc__ = "TRT International."
ChannelEnum.SHOW.__doc__ = "ShowTV."
ChannelEnum.LIGT.__doc__ = "LigTV."
ChannelEnum.TURK.__doc__ = "Türkmax."
ChannelEnum.ATVT.__doc__ = "ATV."
ChannelEnum.FOXT.__doc__ = "Fox Türk."
ChannelEnum.HABN.__doc__ = "HaberTürk."
ChannelEnum.STTV.__doc__ = "Star TV."
ChannelEnum.RRTM.__doc__ = "RTM."
ChannelEnum.RMBC.__doc__ = "MBC."
ChannelEnum.RART.__doc__ = "ART Europe."
ChannelEnum.ARTM.__doc__ = "ART Movie."
ChannelEnum.TVBS.__doc__ = "TVBS Europe."
ChannelEnum.ASIA.__doc__ = "Sony Ent TV MAX."
ChannelEnum.TIVI.__doc__ = "A-Tivi."
ChannelEnum.B4_UM.__doc__ = "B4U Movies."
ChannelEnum.PCNE.__doc__ = "Phoenix CNE."
ChannelEnum.PATN.__doc__ = "ATN."
ChannelEnum.ZEET.__doc__ = "Zee TV."
ChannelEnum.ZEEC.__doc__ = "Zee Cinema."
ChannelEnum.TVE.__doc__ = "TVE."
ChannelEnum.RAI.__doc__ = "Rai Uno."
ChannelEnum.RAID.__doc__ = "Rai Due."
ChannelEnum.RAIT.__doc__ = "Rai Tre."
ChannelEnum.TEVE.__doc__ = "TeVe Sur."
ChannelEnum.ERTS.__doc__ = "ERT Sat."
ChannelEnum.STV.__doc__ = "STV."
ChannelEnum.NTV.__doc__ = "NTV."
ChannelEnum.TVPO.__doc__ = "TV Polonia."
ChannelEnum.NOSJ.__doc__ = "NOS Journaal 24."
ChannelEnum.CULT.__doc__ = "Cultura."
ChannelEnum.VALUE_101.__doc__ = "101."
ChannelEnum.PO24.__doc__ = "Politiek24."
ChannelEnum.HILV.__doc__ = "HilversumBest."
ChannelEnum.HOLL.__doc__ = "Holland Doc."
ChannelEnum.GESC.__doc__ = "/Geschiedenis."
ChannelEnum.VALUE_3_VCN.__doc__ = "3voor12 Central."
ChannelEnum.VALUE_3_VOS.__doc__ = "3voor12 On Stage."
ChannelEnum.STER.__doc__ = "Sterren.nl."
ChannelEnum.NCRV.__doc__ = "Spirit24."
ChannelEnum.OPVO.__doc__ = "Zappelin24/Familie24."
ChannelEnum.CONS.__doc__ = "Consumenten TV."
ChannelEnum.HUMO.__doc__ = "Humor TV."
ChannelEnum.ENTE.__doc__ = "E! Enterntainment."
ChannelEnum.FASH.__doc__ = "Fashion TV."
ChannelEnum.COMC.__doc__ = "Comedy Central/Nickelodeon."
ChannelEnum.TBN.__doc__ = "TBN Europe."
ChannelEnum.DISC.__doc__ = "Discovery Channel."
ChannelEnum.ZONE.__doc__ = "Zone Reality (UK)."
ChannelEnum.ANPL.__doc__ = "Animal Planet."
ChannelEnum.CLUB.__doc__ = "Zone Club."
ChannelEnum.NAGE.__doc__ = "National Geographic/CNBC."
ChannelEnum.TRAC.__doc__ = "Trace TV."
ChannelEnum.NGHD.__doc__ = "National Geographic HD."
ChannelEnum.WILD.__doc__ = "Nat Geo Wild."
ChannelEnum.GARU.__doc__ = "Garuda TV."
ChannelEnum.ZAZA.__doc__ = "Zazaro TV."
ChannelEnum.FAM7.__doc__ = "Family7."
ChannelEnum.DTAL.__doc__ = "Discovery Travel &amp; Living."
ChannelEnum.SCIE.__doc__ = "Discovery Science."
ChannelEnum.CIVI.__doc__ = "Discovery Civilisation."
ChannelEnum.DIHD.__doc__ = "Discovery HD."
ChannelEnum.HIST.__doc__ = "The History Channel."
ChannelEnum.TRAV.__doc__ = "Travel Channel."
ChannelEnum.HETG.__doc__ = "Het Gesprek."
ChannelEnum.GOED.__doc__ = "GoedTV."
ChannelEnum.BABY.__doc__ = "Baby TV (NL)."
ChannelEnum.DH1.__doc__ = "HD-NL."
ChannelEnum.LITV.__doc__ = "Liberty TV."
ChannelEnum.LIVE.__doc__ = "Liveshop."
ChannelEnum.STAR.__doc__ = "Star!"
ChannelEnum.WEER.__doc__ = "Weerkanaal."
ChannelEnum.REAL.__doc__ = "Zone Reality."
ChannelEnum.SCIF.__doc__ = "Sci-Fi Channel."
ChannelEnum.VALUE_13_ST.__doc__ = "13th Street."
ChannelEnum.CARC.__doc__ = "Car Channel."
ChannelEnum.NOSN.__doc__ = "NostalgieNet."
ChannelEnum.HISH.__doc__ = "The History Channel HD."
ChannelEnum.BRHD.__doc__ = "Brava HD."
ChannelEnum.FANT.__doc__ = "Fan TV."
ChannelEnum.RACW.__doc__ = "Raceworld TV."
ChannelEnum.COMF.__doc__ = "Comedy Family."
ChannelEnum.DIER.__doc__ = "AVRO Dier en Natuur."
ChannelEnum.POKE.__doc__ = "Poker Channel."
ChannelEnum.MNET.__doc__ = "Misdaadnet."
ChannelEnum.VOOM.__doc__ = "Voom HD."
ChannelEnum.ZONH.__doc__ = "Zone Horror."
ChannelEnum.KPN1.__doc__ = "Eredivisie Live 1."
ChannelEnum.KPN2.__doc__ = "Eredivisie Live 2."
ChannelEnum.KPN3.__doc__ = "Eredivisie Live 3."
ChannelEnum.KPN4.__doc__ = "Eredivisie Live 4."
ChannelEnum.ZIZO.__doc__ = "PO Zizone TV."
ChannelEnum.DVIC.__doc__ = "Viceland."
ChannelEnum.DVB1.__doc__ = "PO DVB-H 1."
ChannelEnum.DVB2.__doc__ = "PO DVB-H 2."
ChannelEnum.DVB3.__doc__ = "PO DVB-H 3."
ChannelEnum.NICK.__doc__ = "Nickelodeon."
ChannelEnum.NIJN.__doc__ = "Nick Jr."
ChannelEnum.NIKT.__doc__ = "Nick Toons."
ChannelEnum.NIKH.__doc__ = "Nick Hits."
ChannelEnum.CART.__doc__ = "Cartoon Network."
ChannelEnum.BOOM.__doc__ = "Boomerang."
ChannelEnum.CNN.__doc__ = "CNN."
ChannelEnum.BBCW.__doc__ = "BBC World."
ChannelEnum.EURN.__doc__ = "Euronews."
ChannelEnum.SKNE.__doc__ = "Sky News."
ChannelEnum.BLOO.__doc__ = "Bloomberg TV."
ChannelEnum.CNBC.__doc__ = "CNBC Europe."
ChannelEnum.PALJ.__doc__ = "Al Jazeera Arabic."
ChannelEnum.ALJA.__doc__ = "Al Jazeera."
ChannelEnum.FOXN.__doc__ = "Fox News."
ChannelEnum.FXNL.__doc__ = "Fox Nederland."
ChannelEnum.MTV.__doc__ = "MTV."
ChannelEnum.MTV2.__doc__ = "MTV2."
ChannelEnum.HITS.__doc__ = "MTV Hits."
ChannelEnum.BASE.__doc__ = "MTV Base."
ChannelEnum.MTVB.__doc__ = "MTV Brand New."
ChannelEnum.TMF.__doc__ = "TMF."
ChannelEnum.TMFN.__doc__ = "TMF NL."
ChannelEnum.TMFP.__doc__ = "TMF Party."
ChannelEnum.TMFY.__doc__ = "TMF Pure."
ChannelEnum.TVOR.__doc__ = "TV Oranje."
ChannelEnum.VH1_E.__doc__ = "VH-1 (EU)."
ChannelEnum.VH1_C.__doc__ = "VH-1 Classic."
ChannelEnum.PERC.__doc__ = "Performance Channel."
ChannelEnum.MEZZ.__doc__ = "Mezzo."
ChannelEnum.EURO.__doc__ = "Eurosport."
ChannelEnum.EUR2.__doc__ = "Eurosport 2."
ChannelEnum.EXTR.__doc__ = "Extreme Sports Channel (EU)."
ChannelEnum.MOTO.__doc__ = "Motors TV."
ChannelEnum.SAIL.__doc__ = "Sailing channel."
ChannelEnum.ESPN.__doc__ = "ESPN."
ChannelEnum.NASE.__doc__ = "ESPN America."
ChannelEnum.SP11.__doc__ = "Sport1.1."
ChannelEnum.SP12.__doc__ = "Sport1.2."
ChannelEnum.SP13.__doc__ = "Sport1.3."
ChannelEnum.SP14.__doc__ = "Sport1.4."
ChannelEnum.SP15.__doc__ = "Sport1.5."
ChannelEnum.SP16.__doc__ = "Sport1.6."
ChannelEnum.SP17.__doc__ = "Sport1.7."
ChannelEnum.SP18.__doc__ = "Sport1.8."
ChannelEnum.S1_HD.__doc__ = "Sport1 HD."
ChannelEnum.FIL1.__doc__ = "Film1.1 pepe."
ChannelEnum.FIL2.__doc__ = "Film1.2 pepe."
ChannelEnum.FIL3.__doc__ = "Film1.3 pepe."
ChannelEnum.FL11.__doc__ = "Film1.1 DI."
ChannelEnum.FL1_P.__doc__ = "Film1+1 DI."
ChannelEnum.FL12.__doc__ = "Film1.2 DI."
ChannelEnum.FL13.__doc__ = "Film1.3 DI."
ChannelEnum.FLHD.__doc__ = "Film1 HD DI."
ChannelEnum.MGMM.__doc__ = "MGM Movie Channel."
ChannelEnum.TCM.__doc__ = "TCM."
ChannelEnum.HALL.__doc__ = "Hallmark."
ChannelEnum.ACNW.__doc__ = "Action Now!"
ChannelEnum.RHUS.__doc__ = "Hustler TV."
ChannelEnum.PLAY.__doc__ = "Playboy TV."
ChannelEnum.ADUL.__doc__ = "Adult Channel."
ChannelEnum.PSPI.__doc__ = "Private Spice."
ChannelEnum.HUST.__doc__ = "Blue Hustler."
ChannelEnum.OXMO.__doc__ = "PO X-MO."
ChannelEnum.XM24.__doc__ = "X-MO DI."
ChannelEnum.OU24.__doc__ = "PO Out TV."
ChannelEnum.RAD1.__doc__ = "NPO Radio 1."
ChannelEnum.RAD2.__doc__ = "NPO Radio 2."
ChannelEnum.RAD3.__doc__ = "NPO 3FM."
ChannelEnum.RAD4.__doc__ = "NPO Radio 4."
ChannelEnum.RAD5.__doc__ = "NPO Radio 5."
ChannelEnum.RAD6.__doc__ = "NPO Radio 6."
ChannelEnum.REGR.__doc__ = "Regional radio combi-channel."
ChannelEnum.RFRY.__doc__ = "Omrop Fryslân radio."
ChannelEnum.RNOO.__doc__ = "Radio Noord."
ChannelEnum.ROST.__doc__ = "Radio Oost."
ChannelEnum.RGEL.__doc__ = "Radio Gelderland."
ChannelEnum.RFLE.__doc__ = "Radio Flevoland."
ChannelEnum.RBRA.__doc__ = "Omroep Brabant."
ChannelEnum.RUTR.__doc__ = "Radio M Utrecht."
ChannelEnum.RNOH.__doc__ = "Radio Noord-Holland."
ChannelEnum.RWST.__doc__ = "89,3 Radio West."
ChannelEnum.RRIJ.__doc__ = "Radio Rijnmond."
ChannelEnum.LRAD.__doc__ = "L1 Radio."
ChannelEnum.RZEE.__doc__ = "Omroep Zeeland."
ChannelEnum.COMM.__doc__ = "Commercial radio combi-channel."
ChannelEnum.RVER.__doc__ = "Radio Veronica."
ChannelEnum.SLAM.__doc__ = "SLAM! FM."
ChannelEnum.SKYR.__doc__ = "Sky Radio."
ChannelEnum.BNRN.__doc__ = "BNR Nieuwsradio."
ChannelEnum.KINK.__doc__ = "Kink FM."
ChannelEnum.PCAZ.__doc__ = "CAZ!."
ChannelEnum.QMUS.__doc__ = "Qmusic."
ChannelEnum.R538.__doc__ = "Radio 538."
ChannelEnum.GOLD.__doc__ = "Radio 10 Gold."
ChannelEnum.ARRO.__doc__ = "Arrow Classic Rock."
ChannelEnum.FUNX.__doc__ = "FunX."
ChannelEnum.FNXA.__doc__ = "FunX Amsterdam."
ChannelEnum.FNXR.__doc__ = "FunX Rotterdam."
ChannelEnum.FNXU.__doc__ = "FunX Utrecht."
ChannelEnum.FNXD.__doc__ = "FunX Den Haag."
ChannelEnum.FNXAR.__doc__ = "FunX Arab"
ChannelEnum.FNXDA.__doc__ = "FunX Dance"
ChannelEnum.FNXHH.__doc__ = "FunX HipHop"
ChannelEnum.FNXLA.__doc__ = "FunX Latin"
ChannelEnum.FNXRE.__doc__ = "FunX Reggae"
ChannelEnum.FNXSJ.__doc__ = "FunX SlowJamz"
ChannelEnum.CLAS.__doc__ = "Classic FM."
ChannelEnum.BEL1.__doc__ = "VRT/Radio 1."
ChannelEnum.BEL2.__doc__ = "VRT/Radio 2."
ChannelEnum.KLAR.__doc__ = "Klara."
ChannelEnum.BBR1.__doc__ = "BBC Radio 1."
ChannelEnum.BBR2.__doc__ = "BBC Radio 2."
ChannelEnum.BBR3.__doc__ = "BBC Radio 3."
ChannelEnum.BBR4.__doc__ = "BBC Radio 4."
ChannelEnum.BBWS.__doc__ = "BBC Worldservice."
ChannelEnum.BBCX.__doc__ = "BBC 1XTRA."
ChannelEnum.NDR3.__doc__ = "NDR3."
ChannelEnum.WDR4.__doc__ = "WDR 4."
ChannelEnum.WDR3.__doc__ = "WDR3."
ChannelEnum.ONL1.__doc__ = "NPO Online 1"
ChannelEnum.OMEG.__doc__ = "Omega TV"
ChannelEnum.XXXX.__doc__ = (
    "Test channel. This channel only exist for the sake of testing."
)


class ColorType(Enum):
    COLOR = "COLOR"
    BLACK_AND_WHITE = "BLACK AND WHITE"
    BLACK_AND_WHITE_AND_COLOR = "BLACK AND WHITE AND COLOR"
    COLORIZED = "COLORIZED"


class ContentRatingType(Enum):
    DISCRIMINATIE = "DISCRIMINATIE"
    GROF_TAALGEBRUIK = "GROF_TAALGEBRUIK"
    ANGST = "ANGST"
    GEWELD = "GEWELD"
    SEKS = "SEKS"
    DRUGS_EN_ALCOHOL = "DRUGS_EN_ALCOHOL"


ContentRatingType.DISCRIMINATIE.__doc__ = (
    "Discrimination. Contains depictions, or material which may encourage, "
    "discrimination."
)
ContentRatingType.GROF_TAALGEBRUIK.__doc__ = "Coarse language."
ContentRatingType.ANGST.__doc__ = (
    "Fear. May be frightening or scary for young children."
)
ContentRatingType.GEWELD.__doc__ = (
    "Violence. Contains depictions of violence."
)
ContentRatingType.SEKS.__doc__ = (
    "Sex. Contains nudity and/or sexual behavior or sexual references."
)
ContentRatingType.DRUGS_EN_ALCOHOL.__doc__ = (
    "Drugs. Refers to or depicts the use of drugs."
)


@dataclass
class CountryType:
    class Meta:
        name = "countryType"

    value: Optional[str] = field(
        default=None,
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\w){2,4}",
        }
    )


class Encryption(Enum):
    NONE_VALUE = "NONE"
    DRM = "DRM"


@dataclass
class GenreType:
    class Meta:
        name = "genreType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"3(\.[0-9]+)+",
        }
    )


class GeoRestrictionEnum(Enum):
    NL = "NL"
    BENELUX = "BENELUX"
    NLBES = "NLBES"
    NLALL = "NLALL"
    EU = "EU"
    EUROPE = "EUROPE"


GeoRestrictionEnum.NL.__doc__ = "Media only playable in the Netherlands."
GeoRestrictionEnum.BENELUX.__doc__ = (
    "Media only playable in the Benelux (Belgium, Netherlands, Luxembourg). "
    "This is unused."
)
GeoRestrictionEnum.NLBES.__doc__ = "New in 5.6.  Nederland plus BES gemeentes"
GeoRestrictionEnum.NLALL.__doc__ = (
    "New in 5.6. Nederland plus BES gemeentes plus Curacao, St. Maarten en "
    "Aruba"
)
GeoRestrictionEnum.EU.__doc__ = (
    "New in 5.6. EU (incl. BES gemeentes, Curacao, St. Maarten en Aruba)"
)
GeoRestrictionEnum.EUROPE.__doc__ = (
    "New in 5.6. Europa in breedste zin van het woord"
)


class GeoRoleType(Enum):
    RECORDED_IN = "RECORDED_IN"
    SUBJECT = "SUBJECT"
    PRODUCED_IN = "PRODUCED_IN"
    UNDEFINED = "UNDEFINED"


class GroupTypeEnum(Enum):
    STRAND = "STRAND"
    ALBUM = "ALBUM"
    PLAYLIST = "PLAYLIST"
    ARCHIVE = "ARCHIVE"
    COLLECTION = "COLLECTION"
    SEASON = "SEASON"
    SERIES = "SERIES"
    UMBRELLA = "UMBRELLA"


class GtaaStatusType(Enum):
    CANDIDATE = "candidate"
    APPROVED = "approved"
    REDIRECTED = "redirected"
    NOT_COMPLIANT = "not_compliant"
    REJECTED = "rejected"
    OBSOLETE = "obsolete"
    DELETED = "deleted"


class IntentionEnum(Enum):
    INFORM = "INFORM"
    INFORM_NEWS_AND_FACTS = "INFORM_NEWS_AND_FACTS"
    INFORM_INDEPTH = "INFORM_INDEPTH"
    INFORM_GENERAL = "INFORM_GENERAL"
    ENTERTAINMENT = "ENTERTAINMENT"
    ENTERTAINMENT_LEASURE = "ENTERTAINMENT_LEASURE"
    ENTERTAINMENT_INFORMATIVE = "ENTERTAINMENT_INFORMATIVE"
    ACTIVATING = "ACTIVATING"


@dataclass
class LanguageType:
    class Meta:
        name = "languageType"

    value: Optional[str] = field(
        default=None,
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\w){2,4}",
        }
    )


class License(Enum):
    COPYRIGHTED = "COPYRIGHTED"
    PUBLIC_DOMAIN = "PUBLIC_DOMAIN"
    CC_BY = "CC_BY"
    CC_BY_SA = "CC_BY_SA"
    CC_BY_ND = "CC_BY_ND"
    CC_BY_NC = "CC_BY_NC"
    CC_BY_NC_SA = "CC_BY_NC_SA"
    CC_BY_NC_ND = "CC_BY_NC_ND"


class LocationTypeEnum(Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    UNKNOWN = "UNKNOWN"


class MediaTypeEnum(Enum):
    MEDIA = "MEDIA"
    GROUP = "GROUP"
    PROGRAM = "PROGRAM"
    SEGMENTTYPE = "SEGMENTTYPE"
    STRAND = "STRAND"
    ALBUM = "ALBUM"
    PLAYLIST = "PLAYLIST"
    ARCHIVE = "ARCHIVE"
    SEASON = "SEASON"
    SERIES = "SERIES"
    UMBRELLA = "UMBRELLA"
    BROADCAST = "BROADCAST"
    MOVIE = "MOVIE"
    TRAILER = "TRAILER"
    CLIP = "CLIP"
    TRACK = "TRACK"
    SEGMENT = "SEGMENT"
    VISUALRADIO = "VISUALRADIO"
    VISUALRADIOSEGMENT = "VISUALRADIOSEGMENT"
    PROMO = "PROMO"
    RECORDING = "RECORDING"
    COLLECTION = "COLLECTION"


MediaTypeEnum.MEDIA.__doc__ = (
    "The abstract type denoting every possible media type"
)
MediaTypeEnum.GROUP.__doc__ = (
    "The abstract type denoting every possible group type"
)
MediaTypeEnum.PROGRAM.__doc__ = (
    "The abstract type denoting every possible program type"
)
MediaTypeEnum.SEGMENTTYPE.__doc__ = (
    "The abstract type denoting every possible segment type"
)


@dataclass
class OrganizationType:
    class Meta:
        name = "organizationType"

    value: Optional[str] = field(
        default=None,
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )


class PlatformTypeEnum(Enum):
    INTERNETVOD = "INTERNETVOD"
    TVVOD = "TVVOD"
    PLUSVOD = "PLUSVOD"
    NPOPLUSVOD = "NPOPLUSVOD"


@dataclass
class PortalRestrictionType:
    class Meta:
        name = "portalRestrictionType"

    value: Optional[str] = field(
        default=None,
    )
    portal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "portalId",
            "type": "Attribute",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class PredictionStateEnum(Enum):
    NOT_ANNOUNCED = "NOT_ANNOUNCED"
    ANNOUNCED = "ANNOUNCED"
    REALIZED = "REALIZED"
    REVOKED = "REVOKED"


PredictionStateEnum.NOT_ANNOUNCED.__doc__ = (
    "This value is not exposed, it can be present in the database though."
)


class ProgramTypeEnum(Enum):
    BROADCAST = "BROADCAST"
    MOVIE = "MOVIE"
    TRAILER = "TRAILER"
    CLIP = "CLIP"
    STRAND = "STRAND"
    TRACK = "TRACK"
    VISUALRADIO = "VISUALRADIO"
    PROMO = "PROMO"
    RECORDING = "RECORDING"


@dataclass
class RelationType:
    class Meta:
        name = "relationType"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z0-9_-]{4,}",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    uri_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriRef",
            "type": "Attribute",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RepeatType:
    class Meta:
        name = "repeatType"

    value: Optional[str] = field(
        default=None,
    )
    is_rerun: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isRerun",
            "type": "Attribute",
            "required": True,
        }
    )


class RoleType(Enum):
    DIRECTOR = "DIRECTOR"
    CHIEF_EDITOR = "CHIEF_EDITOR"
    EDITOR = "EDITOR"
    PRESENTER = "PRESENTER"
    INTERVIEWER = "INTERVIEWER"
    PRODUCER = "PRODUCER"
    RESEARCH = "RESEARCH"
    GUEST = "GUEST"
    REPORTER = "REPORTER"
    ACTOR = "ACTOR"
    COMMENTATOR = "COMMENTATOR"
    SCRIPTWRITER = "SCRIPTWRITER"
    COMPOSER = "COMPOSER"
    SUBJECT = "SUBJECT"
    PARTICIPANT = "PARTICIPANT"
    SIDEKICK = "SIDEKICK"
    NEWS_PRESENTER = "NEWS_PRESENTER"
    UNDEFINED = "UNDEFINED"


RoleType.SIDEKICK.__doc__ = (
    "Introduced for MediaConnect sync. This is experimental"
)
RoleType.NEWS_PRESENTER.__doc__ = (
    "Introduced for MediaConnect sync. This is experimental"
)


class ScheduleEventTypeEnum(Enum):
    STRAND = "STRAND"


class SegmentTypeEnum(Enum):
    SEGMENT = "SEGMENT"
    VISUALRADIOSEGMENT = "VISUALRADIOSEGMENT"


class StreamingStatusValue(Enum):
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    UNSET = "UNSET"


@dataclass
class TagType:
    class Meta:
        name = "tagType"

    value: Optional[str] = field(
        default=None,
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


class TargetGroupEnum(Enum):
    KIDS_6 = "KIDS_6"
    KIDS_12 = "KIDS_12"
    YOUNG_ADULTS = "YOUNG_ADULTS"
    ADULTS = "ADULTS"
    ADULTS_WITH_KIDS_6 = "ADULTS_WITH_KIDS_6"
    ADULTS_WITH_KIDS_12 = "ADULTS_WITH_KIDS_12"
    EVERYONE = "EVERYONE"


class TextualTypeEnum(Enum):
    MAIN = "MAIN"
    SHORT = "SHORT"
    SUB = "SUB"
    KICKER = "KICKER"
    ORIGINAL = "ORIGINAL"
    EPISODE = "EPISODE"
    WORK = "WORK"
    LEXICO = "LEXICO"
    ABBREVIATION = "ABBREVIATION"


@dataclass
class TwitterType:
    class Meta:
        name = "twitterType"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional["TwitterType.Type"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Type(Enum):
        ACCOUNT = "ACCOUNT"
        HASHTAG = "HASHTAG"


class WorkflowTypeEnum(Enum):
    PUBLISHED = "PUBLISHED"
    REVOKED = "REVOKED"
    FOR_REPUBLICATION = "FOR REPUBLICATION"
    FOR_PUBLICATION = "FOR PUBLICATION"
    DELETED = "DELETED"
    PARENT_REVOKED = "PARENT REVOKED"


@dataclass
class BroadcasterType(OrganizationType):
    class Meta:
        name = "broadcasterType"


@dataclass
class DescendantRefType:
    class Meta:
        name = "descendantRefType"

    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DescriptionType:
    class Meta:
        name = "descriptionType"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GeoLocationType:
    class Meta:
        name = "geoLocationType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    role: Optional[GeoRoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    gtaa_status: Optional[GtaaStatusType] = field(
        default=None,
        metadata={
            "name": "gtaaStatus",
            "type": "Attribute",
        }
    )


@dataclass
class GeoRestrictionType:
    class Meta:
        name = "geoRestrictionType"

    value: Optional[str] = field(
        default=None,
    )
    region_id: Optional[GeoRestrictionEnum] = field(
        default=None,
        metadata={
            "name": "regionId",
            "type": "Attribute",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ImagesType:
    class Meta:
        name = "imagesType"

    image: List[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )


@dataclass
class IntentionType:
    class Meta:
        name = "intentionType"

    intention: List[IntentionEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NameType:
    class Meta:
        name = "nameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    gtaa_status: Optional[GtaaStatusType] = field(
        default=None,
        metadata={
            "name": "gtaaStatus",
            "type": "Attribute",
        }
    )


@dataclass
class PersonType:
    class Meta:
        name = "personType"

    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    gtaa_status: Optional[GtaaStatusType] = field(
        default=None,
        metadata={
            "name": "gtaaStatus",
            "type": "Attribute",
        }
    )


@dataclass
class PortalsType:
    class Meta:
        name = "portalsType"

    portal: List[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class PredictionType:
    class Meta:
        name = "predictionType"

    value: Optional[str] = field(
        default=None,
    )
    state: Optional[PredictionStateEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publish_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )


@dataclass
class RecursiveMemberRef:
    class Meta:
        name = "recursiveMemberRef"

    member_of: List["RecursiveMemberRef"] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    episode_of: List["RecursiveMemberRef"] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment_of: Optional["RecursiveMemberRef"] = field(
        default=None,
        metadata={
            "name": "segmentOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ScheduleEventDescription:
    class Meta:
        name = "scheduleEventDescription"

    value: Optional[str] = field(
        default=None,
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ScheduleEventTitle:
    class Meta:
        name = "scheduleEventTitle"

    value: Optional[str] = field(
        default=None,
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class StreamingStatus:
    class Meta:
        name = "streamingStatus"
        namespace = "urn:vpro:media:2009"

    with_drm: Optional[StreamingStatusValue] = field(
        default=None,
        metadata={
            "name": "withDrm",
            "type": "Attribute",
            "required": True,
        }
    )
    without_drm: Optional[StreamingStatusValue] = field(
        default=None,
        metadata={
            "name": "withoutDrm",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TargetGroupsType:
    class Meta:
        name = "targetGroupsType"

    target_group: List[TargetGroupEnum] = field(
        default_factory=list,
        metadata={
            "name": "targetGroup",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TitleType:
    class Meta:
        name = "titleType"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TopicType:
    class Meta:
        name = "topicType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    gtaa_status: Optional[GtaaStatusType] = field(
        default=None,
        metadata={
            "name": "gtaaStatus",
            "type": "Attribute",
        }
    )


@dataclass
class VideoAttributesType:
    class Meta:
        name = "videoAttributesType"

    color: Optional[ColorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    video_coding: Optional[str] = field(
        default=None,
        metadata={
            "name": "videoCoding",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    aspect_ratio: Optional[AspectRatioEnum] = field(
        default=None,
        metadata={
            "name": "aspectRatio",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    heigth: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "doc": "This obviously is a typo.",
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AvAttributesType:
    class Meta:
        name = "avAttributesType"

    bitrate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    byte_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "byteSize",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    av_file_format: Optional[AvFileFormatEnum] = field(
        default=None,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    video_attributes: Optional[VideoAttributesType] = field(
        default=None,
        metadata={
            "name": "videoAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    audio_attributes: Optional[AudioAttributesType] = field(
        default=None,
        metadata={
            "name": "audioAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class CreditsType:
    class Meta:
        name = "creditsType"

    person: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "sequential": True,
        }
    )
    name: List[NameType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "sequential": True,
        }
    )


@dataclass
class GeoLocationsType:
    class Meta:
        name = "geoLocationsType"

    geo_location: List[GeoLocationType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocation",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MemberRefType:
    class Meta:
        name = "memberRefType"

    episode_of: List[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    member_of: List[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment_of: Optional[RecursiveMemberRef] = field(
        default=None,
        metadata={
            "name": "segmentOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
            "doc": "Reference to the MID of the parent of this object.",
        }
    )
    urn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
            "doc": (
                "Reference to the URN of the parent of this object. URN's are "
                "no longer actively used, but the attribute is\nstill "
                "available for backwards compatibility."
            ),
        }
    )
    crid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "cridRef",
            "type": "Attribute",
            "doc": (
                "Reference to a crid of the parent of this object. This is "
                "only used for imports from systems that cannot\nsupply a MID "
                "or URN. POMS does not export or publish parent crids."
            ),
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    added: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TopicsType:
    class Meta:
        name = "topicsType"

    topic: List[TopicType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LocationType:
    class Meta:
        name = "locationType"

    program_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "programUrl",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    av_attributes: Optional[AvAttributesType] = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    subtitles: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    type: Optional[LocationTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publish_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    publish_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
        }
    )
    creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        }
    )
    last_modified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ScheduleEventType:
    class Meta:
        name = "scheduleEventType"

    title: List[ScheduleEventTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    description: List[ScheduleEventDescription] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    repeat: Optional[RepeatType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    member_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    av_attributes: Optional[AvAttributesType] = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    text_subtitles: Optional[str] = field(
        default=None,
        metadata={
            "name": "textSubtitles",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    text_page: Optional[str] = field(
        default=None,
        metadata={
            "name": "textPage",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    guide_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "guideDay",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    po_prog_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "poProgID",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    primary_lifestyle: Optional[str] = field(
        default=None,
        metadata={
            "name": "primaryLifestyle",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    secondary_lifestyle: Optional[str] = field(
        default=None,
        metadata={
            "name": "secondaryLifestyle",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    imi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    guide_day_attribute: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "guideDay",
            "type": "Attribute",
        }
    )
    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[ScheduleEventTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LocationTableType:
    class Meta:
        name = "locationTableType"

    location: List[LocationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    schedule_event: List[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class LocationsType:
    class Meta:
        name = "locationsType"

    location: List[LocationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class ScheduleEventsType:
    class Meta:
        name = "scheduleEventsType"

    schedule_event: List[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class ScheduleType:
    class Meta:
        name = "scheduleType"

    schedule_event: List[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        }
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    release_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "releaseVersion",
            "type": "Attribute",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reruns: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BaseMediaType:
    """This is the abstract base entity for programs, groups and segments.

    Actually these objects are very similar and share most properties.
    """
    class Meta:
        name = "baseMediaType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "A crid (content reference identifier) is a reference to an "
                "entity in another system. E.g. a crid "
                "like\ncrid://broadcast.radiobox2/335793 refers to a broadcast"
                " with id 335793 in Radiobox. A crid must be a valid\nURI "
                "starting with \"crid://\". Crids must be unique, but they can"
                " be made up freely. It is a good idea to use\na logical "
                "structure which can easily be associated with another system."
                " Any POMS object can have zero or\nmore crids. They can refer"
                " to different systems, but a POMS object could also actually "
                "represent more than\none entity in a remote system."
            ),
        }
    )
    broadcaster: List[BroadcasterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
            "doc": (
                "One or more broadcasters can be the owner of a POMS media "
                "object. This information is meta information about the "
                "object, but it is also used\nfor assigning write access to "
                "the object in the POMS backend to employees of these given "
                "broadcasting companies."
            ),
        }
    )
    portal: List[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "Optionally 'portals' can be assigned to a media object. "
                "Portals are also 'owners', and employees can also work for a "
                "certain portal.\nThis is because some portal are shared by "
                "several broadcasting companies."
            ),
        }
    )
    exclusive: List[PortalRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "Besides having portals, which mainly indicates where the "
                "object originates, a media object can also be assigned "
                "'portal restrictions'.\nIf a media object has any portal "
                "restrictions the media object may only be shown on these "
                "portals."
            ),
        }
    )
    region: List[GeoRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "Media with a geo restriction can only be played in the "
                "indicated region (NL, BENELUX, WORLD). This\nrestriction "
                "doesn't apply to the metadata of the media object. It only "
                "applies to the actual playable content."
            ),
        }
    )
    title: List[TitleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
            "doc": (
                "A media object has one or more titles. All titles have a type"
                " (MAIN, SUB etc.) and an owner (BROADCASTER, MIS etc.).\nThe "
                "combination of type and owner is always unique for a "
                "particular media object, so a media object cannot\nhave "
                "multiple titles of the same type and owner. Titles are sorted"
                " in order of the textualTypeEnum and the in order\nof "
                "ownerTypeEnum when published, so the first title in a "
                "published document will be a title owned by BROADCASTER of "
                "type\nMAIN, if that title exists."
            ),
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "Optional descriptions for the media object. Descriptions have"
                " an owner and a type, and are ordered just like titles."
            ),
        }
    )
    genre: List[GenreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    tag: List[TagType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    intentions: List[IntentionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    target_groups: List[TargetGroupsType] = field(
        default_factory=list,
        metadata={
            "name": "targetGroups",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    geo_locations: List[GeoLocationsType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    topics: List[TopicsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    country: List[CountryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    language: List[LanguageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    is_dubbed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDubbed",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    available_subtitles: List[AvailableSubtitleType] = field(
        default_factory=list,
        metadata={
            "name": "availableSubtitles",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    av_attributes: Optional[AvAttributesType] = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    release_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "releaseYear",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    credits: Optional[CreditsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    award: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    descendant_of: List[DescendantRefType] = field(
        default_factory=list,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    member_of: List[MemberRefType] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    age_rating: Optional[AgeRatingType] = field(
        default=None,
        metadata={
            "name": "ageRating",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    content_rating: List[ContentRatingType] = field(
        default_factory=list,
        metadata={
            "name": "contentRating",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    website: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    twitter: List[TwitterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    teletext: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    prediction: List[PredictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    locations: Optional[LocationsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    relation: List[RelationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    images: Optional[ImagesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    av_type: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "name": "avType",
            "type": "Attribute",
            "required": True,
        }
    )
    sort_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "sortDate",
            "type": "Attribute",
        }
    )
    embeddable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    has_subtitles: bool = field(
        default=False,
        metadata={
            "name": "hasSubtitles",
            "type": "Attribute",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publish_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    publish_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
        }
    )
    creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        }
    )
    last_modified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    merged_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "mergedTo",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )


@dataclass
class Schedule(ScheduleType):
    """Programs of type 'BROADCAST' can contain schedule events.

    A schedule indicates on which channel and at what time the program
    is broadcast. A schedule is a container which contains the schedule
    events of different programs, for a certain period of time.
    """
    class Meta:
        name = "schedule"
        namespace = "urn:vpro:media:2009"


@dataclass
class GroupType(BaseMediaType):
    class Meta:
        name = "groupType"

    po_series_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "poSeriesID",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    is_ordered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isOrdered",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[GroupTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    default_element: Optional[int] = field(
        default=None,
        metadata={
            "name": "defaultElement",
            "type": "Attribute",
        }
    )


@dataclass
class SegmentType(BaseMediaType):
    class Meta:
        name = "segmentType"

    segment_of: Optional[RecursiveMemberRef] = field(
        default=None,
        metadata={
            "name": "segmentOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    start: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[SegmentTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Group(GroupType):
    """A groups collects a number of programs and/or other groups.

    Examples: season, series, playlist and album.
    """
    class Meta:
        name = "group"
        namespace = "urn:vpro:media:2009"


@dataclass
class Segment(SegmentType):
    """A program can contain a number of segments.

    A segment is an identifiable part of a program.
    """
    class Meta:
        name = "segment"
        namespace = "urn:vpro:media:2009"


@dataclass
class SegmentsType:
    class Meta:
        name = "segmentsType"

    segment: List[SegmentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class GroupTableType:
    class Meta:
        name = "groupTableType"

    group: List[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        }
    )


@dataclass
class ProgramType(BaseMediaType):
    class Meta:
        name = "programType"

    schedule_events: Optional[ScheduleEventsType] = field(
        default=None,
        metadata={
            "name": "scheduleEvents",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    episode_of: List[MemberRefType] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "A program (only if its type is 'BROADCAST') can be an episode"
                " of a group of type 'SERIES' or 'SEASON'."
            ),
        }
    )
    segments: Optional[SegmentsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    type: Optional[ProgramTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "doc": "The type of this program (e.g. BROADCAST, TRACK, CLIP)",
        }
    )


@dataclass
class Program(ProgramType):
    """This is the most used entity in POMS.

    It represents e.g. one broadcast program or one web-only clip. It
    represent a standalone entity which a consumer can view or listen
    to.
    """
    class Meta:
        name = "program"
        namespace = "urn:vpro:media:2009"


@dataclass
class ProgramTableType:
    class Meta:
        name = "programTableType"

    program: List[Program] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class MediaTableType:
    class Meta:
        name = "mediaTableType"

    program_table: Optional[ProgramTableType] = field(
        default=None,
        metadata={
            "name": "programTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": "A table with all program objects in this container",
        }
    )
    group_table: Optional[GroupTableType] = field(
        default=None,
        metadata={
            "name": "groupTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": "A table with all group objects in this container",
        }
    )
    location_table: Optional[LocationTableType] = field(
        default=None,
        metadata={
            "name": "locationTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    schedule: Optional[Schedule] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": "A table with all schedule information in this container",
        }
    )
    publisher: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaInformation(MediaTableType):
    """Base element only used when programs, groups and schedule information
    need to be bundled in one XML.

    E.g. when distributing to cable companies.
    """
    class Meta:
        name = "mediaInformation"
        namespace = "urn:vpro:media:2009"
