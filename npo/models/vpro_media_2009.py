from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from npo.models.vpro_shared_2009 import (
    Image,
    OwnerTypeEnum,
    WorkflowEnumType,
)

__NAMESPACE__ = "urn:vpro:media:2009"


class AgeRatingType(Enum):
    """
    :cvar VALUE_6: Suitable for people of age 6 and up.
    :cvar VALUE_9: Suitable for people of age 9 and up.
    :cvar VALUE_12: Suitable for people of age 12 and up.
    :cvar VALUE_14: Suitable for people of age 12 and up.
    :cvar VALUE_16: Suitable for people of age 16 and up.
    :cvar VALUE_18: Suitable for people of age 18 and up.
    :cvar ALL: Suitable for people of all ages.
    :cvar NOT_YET_RATED: Not yet rated
    """
    VALUE_6 = "6"
    VALUE_9 = "9"
    VALUE_12 = "12"
    VALUE_14 = "14"
    VALUE_16 = "16"
    VALUE_18 = "18"
    ALL = "ALL"
    NOT_YET_RATED = "NOT_YET_RATED"


class AspectRatioEnum(Enum):
    """
    :cvar VALUE_4_3:
    :cvar VALUE_16_9:
    """
    VALUE_4_3 = "4:3"
    VALUE_16_9 = "16:9"


@dataclass
class AudioAttributesType:
    """
    :ivar number_of_channels:
    :ivar audio_coding:
    :ivar language:
    """
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
    """
    :cvar MP3:
    :cvar RA:
    :cvar RM:
    :cvar MP4:
    :cvar WVC1:
    :cvar WM:
    :cvar RAM:
    :cvar WMP:
    :cvar HTML:
    :cvar M4_A:
    :cvar M4_V:
    :cvar DGPP:
    :cvar FLV:
    :cvar HASP:
    :cvar MPEG2:
    :cvar H264:
    :cvar UNKNOWN:
    """
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
    """
    :cvar AUDIO:
    :cvar VIDEO:
    :cvar MIXED:
    """
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    MIXED = "MIXED"


@dataclass
class AvailableSubtitleType:
    """
    :ivar language:
    :ivar type:
    """
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
    """
    :cvar NED1: NPO 1.
    :cvar NED2: NPO 2.
    :cvar NED3: NPO 3 &amp; Z@pp.
    :cvar NEDE: Nederland-e.
    :cvar RTL4: RTL 4.
    :cvar RTL5: RTL 5.
    :cvar SBS6: SBS 6.
    :cvar RTL7: RTL 7.
    :cvar VERO: Veronica/Jetix.
    :cvar NET5: Net 5.
    :cvar RTL8: RTL 8.
    :cvar REGI: Regional TV combi-channel.
    :cvar OFRY: Omrop Fryslân tv.
    :cvar NOOR: TV Noord.
    :cvar RTVD: RTV Drenthe.
    :cvar OOST: TV Oost.
    :cvar GELD: TV Gelderland.
    :cvar FLEV: TV Flevoland.
    :cvar BRAB: Omroep Brabant.
    :cvar REGU: Regio TV Utrecht.
    :cvar NORH: TV Noord-Holland.
    :cvar WEST: TV West.
    :cvar RIJN: TV Rijnmond.
    :cvar L1_TV: L1 TV.
    :cvar OZEE: Omroep Zeeland.
    :cvar AT5: AT5.
    :cvar RNN7: RNN7.
    :cvar BVNT: BVN.
    :cvar EEN: Eén.
    :cvar KETN: Ketnet &amp; Canvas.
    :cvar VTM: VTM.
    :cvar KA2: 2BE.
    :cvar VT4: VT4.
    :cvar LUNE: La Une (RTBF 1).
    :cvar LDUE: La Deux (RTBF 2).
    :cvar RTBF: RTBF Sat.
    :cvar ARD: ARD.
    :cvar ZDF: ZDF.
    :cvar WDR: WDR Fehrsehen
    :cvar N_3: N3 (NDR).
    :cvar SUDW: SWF Baden-Württemberg.
    :cvar SWF: SWF Rheinland-Pfalz.
    :cvar RTL: RTL Television.
    :cvar SAT1: Sat1.
    :cvar PRO7: Pro7.
    :cvar VALUE_3_SAT: 3 Sat.
    :cvar KABE: Kabel 1.
    :cvar ARTE: ARTE.
    :cvar T5_ME: TV 5 Monde Europe.
    :cvar FRA2: France 2.
    :cvar FRA3: France 3.
    :cvar BBC1: BBC 1.
    :cvar BBC2: BBC 2.
    :cvar BBTH: BBC Three.
    :cvar BBTC: BBC Three / CBBC.
    :cvar BBCF: BBC Four.
    :cvar BBFC: BBC Four / Ceebies.
    :cvar BBCP: BBC Prime.
    :cvar TRTI: TRT International.
    :cvar SHOW: ShowTV.
    :cvar LIGT: LigTV.
    :cvar TURK: Türkmax.
    :cvar ATVT: ATV.
    :cvar FOXT: Fox Türk.
    :cvar HABN: HaberTürk.
    :cvar STTV: Star TV.
    :cvar RRTM: RTM.
    :cvar RMBC: MBC.
    :cvar RART: ART Europe.
    :cvar ARTM: ART Movie.
    :cvar TVBS: TVBS Europe.
    :cvar ASIA: Sony Ent TV MAX.
    :cvar TIVI: A-Tivi.
    :cvar B4_UM: B4U Movies.
    :cvar PCNE: Phoenix CNE.
    :cvar PATN: ATN.
    :cvar ZEET: Zee TV.
    :cvar ZEEC: Zee Cinema.
    :cvar TVE: TVE.
    :cvar RAI: Rai Uno.
    :cvar RAID: Rai Due.
    :cvar RAIT: Rai Tre.
    :cvar TEVE: TeVe Sur.
    :cvar ERTS: ERT Sat.
    :cvar STV: STV.
    :cvar NTV: NTV.
    :cvar TVPO: TV Polonia.
    :cvar NOSJ: NOS Journaal 24.
    :cvar CULT: Cultura.
    :cvar VALUE_101: 101.
    :cvar PO24: Politiek24.
    :cvar HILV: HilversumBest.
    :cvar HOLL: Holland Doc.
    :cvar GESC: /Geschiedenis.
    :cvar VALUE_3_VCN: 3voor12 Central.
    :cvar VALUE_3_VOS: 3voor12 On Stage.
    :cvar STER: Sterren.nl.
    :cvar NCRV: Spirit24.
    :cvar OPVO: Zappelin24/Familie24.
    :cvar CONS: Consumenten TV.
    :cvar HUMO: Humor TV.
    :cvar ENTE: E! Enterntainment.
    :cvar FASH: Fashion TV.
    :cvar COMC: Comedy Central/Nickelodeon.
    :cvar TBN: TBN Europe.
    :cvar DISC: Discovery Channel.
    :cvar ZONE: Zone Reality (UK).
    :cvar ANPL: Animal Planet.
    :cvar CLUB: Zone Club.
    :cvar NAGE: National Geographic/CNBC.
    :cvar TRAC: Trace TV.
    :cvar NGHD: National Geographic HD.
    :cvar WILD: Nat Geo Wild.
    :cvar GARU: Garuda TV.
    :cvar ZAZA: Zazaro TV.
    :cvar FAM7: Family7.
    :cvar DTAL: Discovery Travel &amp; Living.
    :cvar SCIE: Discovery Science.
    :cvar CIVI: Discovery Civilisation.
    :cvar DIHD: Discovery HD.
    :cvar HIST: The History Channel.
    :cvar TRAV: Travel Channel.
    :cvar HETG: Het Gesprek.
    :cvar GOED: GoedTV.
    :cvar BABY: Baby TV (NL).
    :cvar DH1: HD-NL.
    :cvar LITV: Liberty TV.
    :cvar LIVE: Liveshop.
    :cvar STAR: Star!
    :cvar WEER: Weerkanaal.
    :cvar REAL: Zone Reality.
    :cvar SCIF: Sci-Fi Channel.
    :cvar VALUE_13_ST: 13th Street.
    :cvar CARC: Car Channel.
    :cvar NOSN: NostalgieNet.
    :cvar HISH: The History Channel HD.
    :cvar BRHD: Brava HD.
    :cvar FANT: Fan TV.
    :cvar RACW: Raceworld TV.
    :cvar COMF: Comedy Family.
    :cvar DIER: AVRO Dier en Natuur.
    :cvar POKE: Poker Channel.
    :cvar MNET: Misdaadnet.
    :cvar VOOM: Voom HD.
    :cvar ZONH: Zone Horror.
    :cvar KPN1: Eredivisie Live 1.
    :cvar KPN2: Eredivisie Live 2.
    :cvar KPN3: Eredivisie Live 3.
    :cvar KPN4: Eredivisie Live 4.
    :cvar ZIZO: PO Zizone TV.
    :cvar DVIC: Viceland.
    :cvar DVB1: PO DVB-H 1.
    :cvar DVB2: PO DVB-H 2.
    :cvar DVB3: PO DVB-H 3.
    :cvar NICK: Nickelodeon.
    :cvar NIJN: Nick Jr.
    :cvar NIKT: Nick Toons.
    :cvar NIKH: Nick Hits.
    :cvar CART: Cartoon Network.
    :cvar BOOM: Boomerang.
    :cvar CNN: CNN.
    :cvar BBCW: BBC World.
    :cvar EURN: Euronews.
    :cvar SKNE: Sky News.
    :cvar BLOO: Bloomberg TV.
    :cvar CNBC: CNBC Europe.
    :cvar PALJ: Al Jazeera Arabic.
    :cvar ALJA: Al Jazeera.
    :cvar FOXN: Fox News.
    :cvar FXNL: Fox Nederland.
    :cvar MTV: MTV.
    :cvar MTV2: MTV2.
    :cvar HITS: MTV Hits.
    :cvar BASE: MTV Base.
    :cvar MTVB: MTV Brand New.
    :cvar TMF: TMF.
    :cvar TMFN: TMF NL.
    :cvar TMFP: TMF Party.
    :cvar TMFY: TMF Pure.
    :cvar TVOR: TV Oranje.
    :cvar VH1_E: VH-1 (EU).
    :cvar VH1_C: VH-1 Classic.
    :cvar PERC: Performance Channel.
    :cvar MEZZ: Mezzo.
    :cvar EURO: Eurosport.
    :cvar EUR2: Eurosport 2.
    :cvar EXTR: Extreme Sports Channel (EU).
    :cvar MOTO: Motors TV.
    :cvar SAIL: Sailing channel.
    :cvar ESPN: ESPN.
    :cvar NASE: ESPN America.
    :cvar SP11: Sport1.1.
    :cvar SP12: Sport1.2.
    :cvar SP13: Sport1.3.
    :cvar SP14: Sport1.4.
    :cvar SP15: Sport1.5.
    :cvar SP16: Sport1.6.
    :cvar SP17: Sport1.7.
    :cvar SP18: Sport1.8.
    :cvar S1_HD: Sport1 HD.
    :cvar FIL1: Film1.1 pepe.
    :cvar FIL2: Film1.2 pepe.
    :cvar FIL3: Film1.3 pepe.
    :cvar FL11: Film1.1 DI.
    :cvar FL1_P: Film1+1 DI.
    :cvar FL12: Film1.2 DI.
    :cvar FL13: Film1.3 DI.
    :cvar FLHD: Film1 HD DI.
    :cvar MGMM: MGM Movie Channel.
    :cvar TCM: TCM.
    :cvar HALL: Hallmark.
    :cvar ACNW: Action Now!
    :cvar RHUS: Hustler TV.
    :cvar PLAY: Playboy TV.
    :cvar ADUL: Adult Channel.
    :cvar PSPI: Private Spice.
    :cvar HUST: Blue Hustler.
    :cvar OXMO: PO X-MO.
    :cvar XM24: X-MO DI.
    :cvar OU24: PO Out TV.
    :cvar RAD1: NPO Radio 1.
    :cvar RAD2: NPO Radio 2.
    :cvar R2_SJ:
    :cvar RAD3: NPO 3FM.
    :cvar R3_KX:
    :cvar RAD4: NPO Radio 4.
    :cvar R4_CO:
    :cvar RAD5: NPO Radio 5.
    :cvar R5_ST:
    :cvar RAD6: NPO Radio 6.
    :cvar REGR: Regional radio combi-channel.
    :cvar RFRY: Omrop Fryslân radio.
    :cvar RNOO: Radio Noord.
    :cvar ROST: Radio Oost.
    :cvar RGEL: Radio Gelderland.
    :cvar RFLE: Radio Flevoland.
    :cvar RBRA: Omroep Brabant.
    :cvar RUTR: Radio M Utrecht.
    :cvar RNOH: Radio Noord-Holland.
    :cvar RWST: 89,3 Radio West.
    :cvar RRIJ: Radio Rijnmond.
    :cvar LRAD: L1 Radio.
    :cvar RZEE: Omroep Zeeland.
    :cvar COMM: Commercial radio combi-channel.
    :cvar RVER: Radio Veronica.
    :cvar SLAM: SLAM! FM.
    :cvar SKYR: Sky Radio.
    :cvar BNRN: BNR Nieuwsradio.
    :cvar KINK: Kink FM.
    :cvar PCAZ: CAZ!.
    :cvar QMUS: Qmusic.
    :cvar R538: Radio 538.
    :cvar GOLD: Radio 10 Gold.
    :cvar ARRO: Arrow Classic Rock.
    :cvar FUNX: FunX.
    :cvar FNXA: FunX Amsterdam.
    :cvar FNXR: FunX Rotterdam.
    :cvar FNXU: FunX Utrecht.
    :cvar FNXD: FunX Den Haag.
    :cvar FNXAR: FunX Arab
    :cvar FNXDA: FunX Dance
    :cvar FNXHH: FunX HipHop
    :cvar FNXLA: FunX Latin
    :cvar FNXRE: FunX Reggae
    :cvar FNXSJ: FunX SlowJamz
    :cvar CLAS: Classic FM.
    :cvar BEL1: VRT/Radio 1.
    :cvar BEL2: VRT/Radio 2.
    :cvar KLAR: Klara.
    :cvar BBR1: BBC Radio 1.
    :cvar BBR2: BBC Radio 2.
    :cvar BBR3: BBC Radio 3.
    :cvar BBR4: BBC Radio 4.
    :cvar BBWS: BBC Worldservice.
    :cvar BBCX: BBC 1XTRA.
    :cvar NDR3: NDR3.
    :cvar WDR4: WDR 4.
    :cvar WDR3: WDR3.
    :cvar ONL1: NPO Online 1
    :cvar OMEG: Omega TV
    :cvar D24_K:
    :cvar H1_NL:
    :cvar SYFY:
    :cvar SBS9:
    :cvar DIXD:
    :cvar BRNL:
    :cvar FOXL:
    :cvar TLC:
    :cvar BCFS:
    :cvar AMC:
    :cvar FLM1:
    :cvar ZGS1:
    :cvar BRTZ:
    :cvar RTLF:
    :cvar TVDR:
    :cvar VRTC:
    :cvar XXXX: Test channel. This channel only exist for the sake of testing.
    """
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


class ColorType(Enum):
    """
    :cvar COLOR:
    :cvar BLACK_AND_WHITE:
    :cvar BLACK_AND_WHITE_AND_COLOR:
    :cvar COLORIZED:
    """
    COLOR = "COLOR"
    BLACK_AND_WHITE = "BLACK AND WHITE"
    BLACK_AND_WHITE_AND_COLOR = "BLACK AND WHITE AND COLOR"
    COLORIZED = "COLORIZED"


class ContentRatingType(Enum):
    """
    :cvar DISCRIMINATIE: Discrimination. Contains depictions, or material which may encourage, discrimination.
    :cvar GROF_TAALGEBRUIK: Coarse language.
    :cvar ANGST: Fear. May be frightening or scary for young children.
    :cvar GEWELD: Violence. Contains depictions of violence.
    :cvar SEKS: Sex. Contains nudity and/or sexual behavior or sexual references.
    :cvar DRUGS_EN_ALCOHOL: Drugs. Refers to or depicts the use of drugs.
    """
    DISCRIMINATIE = "DISCRIMINATIE"
    GROF_TAALGEBRUIK = "GROF_TAALGEBRUIK"
    ANGST = "ANGST"
    GEWELD = "GEWELD"
    SEKS = "SEKS"
    DRUGS_EN_ALCOHOL = "DRUGS_EN_ALCOHOL"


@dataclass
class CountryType:
    """
    :ivar value:
    :ivar code:
    """
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
    """
    :cvar NONE_VALUE:
    :cvar DRM:
    """
    NONE_VALUE = "NONE"
    DRM = "DRM"


@dataclass
class GenreType:
    """
    :ivar term:
    :ivar id:
    """
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
    """
    :cvar NL: Media only playable in the Netherlands.
    :cvar BENELUX: Media only playable in the Benelux (Belgium, Netherlands, Luxembourg). This is unused.
    :cvar NLBES: New in 5.6.  Nederland plus BES gemeentes
    :cvar NLALL: New in 5.6. Nederland plus BES gemeentes plus Curacao, St. Maarten en Aruba
    :cvar EU: New in 5.6. EU (incl. BES gemeentes, Curacao, St. Maarten en Aruba)
    :cvar EUROPE: New in 5.6. Europa in breedste zin van het woord
    """
    NL = "NL"
    BENELUX = "BENELUX"
    NLBES = "NLBES"
    NLALL = "NLALL"
    EU = "EU"
    EUROPE = "EUROPE"


class GeoRoleType(Enum):
    """
    :cvar RECORDED_IN:
    :cvar SUBJECT:
    :cvar PRODUCED_IN:
    :cvar UNDEFINED:
    """
    RECORDED_IN = "RECORDED_IN"
    SUBJECT = "SUBJECT"
    PRODUCED_IN = "PRODUCED_IN"
    UNDEFINED = "UNDEFINED"


class GroupTypeEnum(Enum):
    """
    :cvar STRAND:
    :cvar ALBUM:
    :cvar PLAYLIST:
    :cvar ARCHIVE:
    :cvar COLLECTION:
    :cvar SEASON:
    :cvar SERIES:
    :cvar UMBRELLA:
    """
    STRAND = "STRAND"
    ALBUM = "ALBUM"
    PLAYLIST = "PLAYLIST"
    ARCHIVE = "ARCHIVE"
    COLLECTION = "COLLECTION"
    SEASON = "SEASON"
    SERIES = "SERIES"
    UMBRELLA = "UMBRELLA"


class GtaaStatusType(Enum):
    """
    :cvar CANDIDATE:
    :cvar APPROVED:
    :cvar REDIRECTED:
    :cvar NOT_COMPLIANT:
    :cvar REJECTED:
    :cvar OBSOLETE:
    :cvar DELETED:
    """
    CANDIDATE = "candidate"
    APPROVED = "approved"
    REDIRECTED = "redirected"
    NOT_COMPLIANT = "not_compliant"
    REJECTED = "rejected"
    OBSOLETE = "obsolete"
    DELETED = "deleted"


class IntentionEnum(Enum):
    """
    :cvar INFORM:
    :cvar INFORM_NEWS_AND_FACTS:
    :cvar INFORM_INDEPTH:
    :cvar INFORM_GENERAL:
    :cvar ENTERTAINMENT:
    :cvar ENTERTAINMENT_LEASURE:
    :cvar ENTERTAINMENT_INFORMATIVE:
    :cvar ACTIVATING:
    """
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
    """
    :ivar value:
    :ivar code:
    """
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
    """
    :cvar COPYRIGHTED:
    :cvar PUBLIC_DOMAIN:
    :cvar CC_BY:
    :cvar CC_BY_SA:
    :cvar CC_BY_ND:
    :cvar CC_BY_NC:
    :cvar CC_BY_NC_SA:
    :cvar CC_BY_NC_ND:
    """
    COPYRIGHTED = "COPYRIGHTED"
    PUBLIC_DOMAIN = "PUBLIC_DOMAIN"
    CC_BY = "CC_BY"
    CC_BY_SA = "CC_BY_SA"
    CC_BY_ND = "CC_BY_ND"
    CC_BY_NC = "CC_BY_NC"
    CC_BY_NC_SA = "CC_BY_NC_SA"
    CC_BY_NC_ND = "CC_BY_NC_ND"


class LocationTypeEnum(Enum):
    """
    :cvar INTERNAL:
    :cvar EXTERNAL:
    :cvar UNKNOWN:
    """
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    UNKNOWN = "UNKNOWN"


class MediaTypeEnum(Enum):
    """
    :cvar MEDIA: The abstract type denoting every possible media type
    :cvar GROUP: The abstract type denoting every possible group type
    :cvar PROGRAM: The abstract type denoting every possible program type
    :cvar SEGMENTTYPE: The abstract type denoting every possible segment type
    :cvar STRAND:
    :cvar ALBUM:
    :cvar PLAYLIST:
    :cvar ARCHIVE:
    :cvar SEASON:
    :cvar SERIES:
    :cvar UMBRELLA:
    :cvar BROADCAST:
    :cvar MOVIE:
    :cvar TRAILER:
    :cvar CLIP:
    :cvar TRACK:
    :cvar SEGMENT:
    :cvar VISUALRADIO:
    :cvar VISUALRADIOSEGMENT:
    :cvar PROMO:
    :cvar RECORDING:
    :cvar COLLECTION:
    """
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


@dataclass
class OrganizationType:
    """
    :ivar value:
    :ivar id:
    """
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
    """
    :cvar INTERNETVOD:
    :cvar TVVOD:
    :cvar PLUSVOD:
    :cvar NPOPLUSVOD:
    """
    INTERNETVOD = "INTERNETVOD"
    TVVOD = "TVVOD"
    PLUSVOD = "PLUSVOD"
    NPOPLUSVOD = "NPOPLUSVOD"


@dataclass
class PortalRestrictionType:
    """
    :ivar value:
    :ivar portal_id:
    :ivar start:
    :ivar stop:
    """
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
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class PredictionStateEnum(Enum):
    """
    :cvar NOT_ANNOUNCED: This value is not exposed, it can be present in the database though.
    :cvar ANNOUNCED:
    :cvar REALIZED:
    :cvar REVOKED:
    """
    NOT_ANNOUNCED = "NOT_ANNOUNCED"
    ANNOUNCED = "ANNOUNCED"
    REALIZED = "REALIZED"
    REVOKED = "REVOKED"


class ProgramTypeEnum(Enum):
    """
    :cvar BROADCAST:
    :cvar MOVIE:
    :cvar TRAILER:
    :cvar CLIP:
    :cvar STRAND:
    :cvar TRACK:
    :cvar VISUALRADIO:
    :cvar PROMO:
    :cvar RECORDING:
    """
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
    """
    :ivar value:
    :ivar type:
    :ivar broadcaster:
    :ivar uri_ref:
    :ivar urn:
    """
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
    """
    :ivar value:
    :ivar is_rerun:
    """
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
    """
    :cvar DIRECTOR:
    :cvar CHIEF_EDITOR:
    :cvar EDITOR:
    :cvar PRESENTER:
    :cvar INTERVIEWER:
    :cvar PRODUCER:
    :cvar RESEARCH:
    :cvar GUEST:
    :cvar REPORTER:
    :cvar ACTOR:
    :cvar COMMENTATOR:
    :cvar SCRIPTWRITER:
    :cvar COMPOSER:
    :cvar SUBJECT:
    :cvar PARTICIPANT:
    :cvar SIDEKICK: Introduced for MediaConnect sync. This is experimental
    :cvar NEWS_PRESENTER: Introduced for MediaConnect sync. This is experimental
    :cvar UNDEFINED:
    """
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


class ScheduleEventTypeEnum(Enum):
    """
    :cvar STRAND:
    """
    STRAND = "STRAND"


class SegmentTypeEnum(Enum):
    """
    :cvar SEGMENT:
    :cvar VISUALRADIOSEGMENT:
    """
    SEGMENT = "SEGMENT"
    VISUALRADIOSEGMENT = "VISUALRADIOSEGMENT"


class StreamingStatusValue(Enum):
    """
    :cvar OFFLINE:
    :cvar ONLINE:
    :cvar UNSET:
    """
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    UNSET = "UNSET"


@dataclass
class TagType:
    """
    :ivar value:
    :ivar lang:
    """
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
    """
    :cvar KIDS_6:
    :cvar KIDS_12:
    :cvar YOUNG_ADULTS:
    :cvar ADULTS:
    :cvar ADULTS_WITH_KIDS_6:
    :cvar ADULTS_WITH_KIDS_12:
    :cvar EVERYONE:
    """
    KIDS_6 = "KIDS_6"
    KIDS_12 = "KIDS_12"
    YOUNG_ADULTS = "YOUNG_ADULTS"
    ADULTS = "ADULTS"
    ADULTS_WITH_KIDS_6 = "ADULTS_WITH_KIDS_6"
    ADULTS_WITH_KIDS_12 = "ADULTS_WITH_KIDS_12"
    EVERYONE = "EVERYONE"


class TextualTypeEnum(Enum):
    """
    :cvar MAIN:
    :cvar SHORT:
    :cvar SUB:
    :cvar KICKER:
    :cvar ORIGINAL:
    :cvar EPISODE:
    :cvar WORK:
    :cvar LEXICO:
    :cvar ABBREVIATION:
    """
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
    """
    :ivar value:
    :ivar type:
    """
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
        """
        :cvar ACCOUNT:
        :cvar HASHTAG:
        """
        ACCOUNT = "ACCOUNT"
        HASHTAG = "HASHTAG"


class WorkflowTypeEnum(Enum):
    """
    :cvar PUBLISHED:
    :cvar REVOKED:
    :cvar FOR_REPUBLICATION:
    :cvar FOR_PUBLICATION:
    :cvar DELETED:
    :cvar PARENT_REVOKED:
    """
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
    """
    :ivar mid_ref:
    :ivar urn_ref:
    :ivar type:
    """
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
    """
    :ivar value:
    :ivar type:
    :ivar owner:
    """
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
    """
    :ivar name:
    :ivar scope_note:
    :ivar role:
    :ivar gtaa_uri:
    :ivar gtaa_status:
    """
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
    """
    :ivar value:
    :ivar region_id:
    :ivar start:
    :ivar stop:
    :ivar platform:
    """
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
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[str] = field(
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
    """
    :ivar image:
    """
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
    """
    :ivar intention:
    :ivar owner:
    """
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
    """
    :ivar name:
    :ivar scope_note:
    :ivar role:
    :ivar gtaa_uri:
    :ivar gtaa_status:
    """
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
    """
    :ivar given_name:
    :ivar family_name:
    :ivar role:
    :ivar gtaa_uri:
    :ivar gtaa_status:
    """
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
    """
    :ivar portal:
    """
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
    """
    :ivar value:
    :ivar state:
    :ivar publish_start:
    :ivar publish_stop:
    """
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
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )


@dataclass
class RecursiveMemberRef:
    """
    :ivar member_of:
    :ivar episode_of:
    :ivar segment_of:
    :ivar mid_ref:
    :ivar type:
    :ivar index:
    :ivar highlighted:
    """
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
    """
    :ivar value:
    :ivar owner:
    :ivar type:
    """
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
    """
    :ivar value:
    :ivar owner:
    :ivar type:
    """
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
    """
    :ivar with_drm:
    :ivar without_drm:
    """
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
    """
    :ivar target_group:
    :ivar owner:
    """
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
    """
    :ivar value:
    :ivar type:
    :ivar owner:
    """
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
    """
    :ivar name:
    :ivar scope_note:
    :ivar gtaa_uri:
    :ivar gtaa_status:
    """
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
    """
    :ivar color:
    :ivar video_coding:
    :ivar aspect_ratio:
    :ivar height:
    :ivar heigth: This obviously is a typo.
    :ivar width:
    """
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
    """
    :ivar bitrate:
    :ivar byte_size:
    :ivar av_file_format:
    :ivar video_attributes:
    :ivar audio_attributes:
    """
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
    """
    :ivar person:
    :ivar name:
    """
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
    """
    :ivar geo_location:
    :ivar owner:
    """
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
    """
    :ivar episode_of:
    :ivar member_of:
    :ivar segment_of:
    :ivar mid_ref: Reference to the MID of the parent of this object.
    :ivar urn_ref: Reference to the URN of the parent of this object. URN's are no longer actively used, but the attribute is
              still available for backwards compatibility.
    :ivar crid_ref: Reference to a crid of the parent of this object. This is only used for imports from systems that cannot
              supply a MID or URN. POMS does not export or publish parent crids.
    :ivar type:
    :ivar index:
    :ivar highlighted:
    :ivar added:
    """
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
        }
    )
    urn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
        }
    )
    crid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "cridRef",
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
    added: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TopicsType:
    """
    :ivar topic:
    :ivar owner:
    """
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
    """
    :ivar program_url:
    :ivar av_attributes:
    :ivar subtitles:
    :ivar offset:
    :ivar duration:
    :ivar type:
    :ivar platform:
    :ivar owner:
    :ivar urn:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar publish_date:
    :ivar creation_date:
    :ivar last_modified:
    :ivar workflow:
    """
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
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[str] = field(
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
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    publish_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
        }
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        }
    )
    last_modified: Optional[str] = field(
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
    """
    :ivar title:
    :ivar description:
    :ivar repeat:
    :ivar member_of:
    :ivar av_attributes:
    :ivar text_subtitles:
    :ivar text_page:
    :ivar guide_day:
    :ivar start:
    :ivar offset:
    :ivar duration:
    :ivar po_prog_id:
    :ivar primary_lifestyle:
    :ivar secondary_lifestyle:
    :ivar imi:
    :ivar channel:
    :ivar net:
    :ivar guide_day_attribute:
    :ivar mid_ref:
    :ivar urn_ref:
    :ivar type:
    """
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
    guide_day: Optional[str] = field(
        default=None,
        metadata={
            "name": "guideDay",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[str] = field(
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
    guide_day_attribute: Optional[str] = field(
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
    """
    :ivar location:
    :ivar schedule_event:
    """
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
    """
    :ivar location:
    """
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
    """
    :ivar schedule_event:
    """
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
    """
    :ivar schedule_event:
    :ivar channel:
    :ivar net:
    :ivar date:
    :ivar release_version:
    :ivar start:
    :ivar stop:
    :ivar reruns:
    """
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
    date: Optional[str] = field(
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
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[str] = field(
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
    """This is the abstract base entity for programs, groups and segments. Actually
    these objects are very similar and share most properties.

    :ivar crid: A crid (content reference identifier) is a reference to an entity in another system. E.g. a crid like
                crid://broadcast.radiobox2/335793 refers to a broadcast with id 335793 in Radiobox. A crid must be a valid
                URI starting with "crid://". Crids must be unique, but they can be made up freely. It is a good idea to use
                a logical structure which can easily be associated with another system. Any POMS object can have zero or
                more crids. They can refer to different systems, but a POMS object could also actually represent more than
                one entity in a remote system.
    :ivar broadcaster: One or more broadcasters can be the owner of a POMS media object. This information is meta information about the object, but it is also used
                for assigning write access to the object in the POMS backend to employees of these given broadcasting companies.
    :ivar portal: Optionally 'portals' can be assigned to a media object. Portals are also 'owners', and employees can also work for a certain portal.
                This is because some portal are shared by several broadcasting companies.
    :ivar exclusive: Besides having portals, which mainly indicates where the object originates, a media object can also be assigned 'portal restrictions'.
                If a media object has any portal restrictions the media object may only be shown on these portals.
    :ivar region: Media with a geo restriction can only be played in the indicated region (NL, BENELUX, WORLD). This
                restriction doesn't apply to the metadata of the media object. It only applies to the actual playable content.
    :ivar title: A media object has one or more titles. All titles have a type (MAIN, SUB etc.) and an owner (BROADCASTER, MIS etc.).
                The combination of type and owner is always unique for a particular media object, so a media object cannot
                have multiple titles of the same type and owner. Titles are sorted in order of the textualTypeEnum and the in order
                of ownerTypeEnum when published, so the first title in a published document will be a title owned by BROADCASTER of type
                MAIN, if that title exists.
    :ivar description: Optional descriptions for the media object. Descriptions have an owner and a type, and are ordered just like titles.
    :ivar genre:
    :ivar tag:
    :ivar intentions:
    :ivar target_groups:
    :ivar geo_locations:
    :ivar topics:
    :ivar source:
    :ivar country:
    :ivar language:
    :ivar is_dubbed:
    :ivar available_subtitles:
    :ivar av_attributes:
    :ivar release_year:
    :ivar duration:
    :ivar credits:
    :ivar award:
    :ivar descendant_of:
    :ivar member_of:
    :ivar age_rating:
    :ivar content_rating:
    :ivar email:
    :ivar website:
    :ivar twitter:
    :ivar teletext:
    :ivar prediction:
    :ivar locations:
    :ivar relation:
    :ivar images:
    :ivar mid:
    :ivar av_type:
    :ivar sort_date:
    :ivar embeddable:
    :ivar has_subtitles:
    :ivar urn:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar publish_date:
    :ivar creation_date:
    :ivar last_modified:
    :ivar workflow:
    :ivar merged_to:
    """
    class Meta:
        name = "baseMediaType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    broadcaster: List[BroadcasterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        }
    )
    portal: List[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    exclusive: List[PortalRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    region: List[GeoRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    title: List[TitleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
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
    duration: Optional[str] = field(
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
    sort_date: Optional[str] = field(
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
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    publish_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
        }
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        }
    )
    last_modified: Optional[str] = field(
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

    A schedule indicates on which channel and at what time the program is
    broadcast. A schedule is a container which contains the schedule events
    of different programs, for a certain period of time.
    """
    class Meta:
        name = "schedule"
        namespace = "urn:vpro:media:2009"


@dataclass
class GroupType(BaseMediaType):
    """
    :ivar po_series_id:
    :ivar is_ordered:
    :ivar type:
    :ivar default_element:
    """
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
    """
    :ivar segment_of:
    :ivar start:
    :ivar mid_ref:
    :ivar urn_ref:
    :ivar type:
    """
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
    start: Optional[str] = field(
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
    """
    :ivar segment:
    """
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
    """
    :ivar group:
    """
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
    """
    :ivar schedule_events:
    :ivar episode_of: A program (only if its type is 'BROADCAST') can be an episode of a group of type 'SERIES' or 'SEASON'.
    :ivar segments:
    :ivar type: The type of this program (e.g. BROADCAST, TRACK, CLIP)
    """
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
        }
    )


@dataclass
class Program(ProgramType):
    """This is the most used entity in POMS.

    It represents e.g. one broadcast program or one web-only clip. It
    represent a standalone entity which a consumer can view or listen to.
    """
    class Meta:
        name = "program"
        namespace = "urn:vpro:media:2009"


@dataclass
class ProgramTableType:
    """
    :ivar program:
    """
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
    """
    :ivar program_table: A table with all program objects in this container
    :ivar group_table: A table with all group objects in this container
    :ivar location_table:
    :ivar schedule: A table with all schedule information in this container
    :ivar publisher:
    :ivar publication_time:
    :ivar version:
    """
    class Meta:
        name = "mediaTableType"

    program_table: Optional[ProgramTableType] = field(
        default=None,
        metadata={
            "name": "programTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    group_table: Optional[GroupTableType] = field(
        default=None,
        metadata={
            "name": "groupTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
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
        }
    )
    publisher: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publication_time: Optional[str] = field(
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
    """Base element only used when programs, groups and schedule information need
    to be bundled in one XML.

    E.g. when distributing to cable companies.
    """
    class Meta:
        name = "mediaInformation"
        namespace = "urn:vpro:media:2009"
