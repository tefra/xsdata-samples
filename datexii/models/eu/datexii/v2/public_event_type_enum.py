from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PublicEventTypeEnum(Enum):
    """
    Types of public events.

    :cvar AGRICULTURAL_SHOW: Agricultural show or event which could
        disrupt traffic.
    :cvar AIR_SHOW: Air show or other aeronautical event which could
        disrupt traffic.
    :cvar ATHLETICS_MEETING: Athletics event that could disrupt traffic.
    :cvar COMMERCIAL_EVENT: Commercial event which could disrupt
        traffic.
    :cvar CULTURAL_EVENT: Cultural event which could disrupt traffic.
    :cvar BALL_GAME: Ball game event that could disrupt traffic.
    :cvar BASEBALL_GAME: Baseball game event that could disrupt traffic.
    :cvar BASKETBALL_GAME: Basketball game event that could disrupt
        traffic.
    :cvar BICYCLE_RACE: Bicycle race that could disrupt traffic.
    :cvar BOAT_RACE: Regatta (boat race event of sailing, powerboat or
        rowing) that could disrupt traffic.
    :cvar BOAT_SHOW: Boat show which could disrupt traffic.
    :cvar BOXING_TOURNAMENT: Boxing event that could disrupt traffic.
    :cvar BULL_FIGHT: Bull fighting event that could disrupt traffic.
    :cvar CEREMONIAL_EVENT: Formal or religious act, rite or ceremony
        that could disrupt traffic.
    :cvar CONCERT: Concert event that could disrupt traffic.
    :cvar CRICKET_MATCH: Cricket match that could disrupt traffic.
    :cvar EXHIBITION: Major display or trade show which could disrupt
        traffic.
    :cvar FAIR: Periodic (e.g. annual), often traditional, gathering for
        entertainment or trade promotion, which could disrupt traffic.
    :cvar FESTIVAL: Celebratory event or series of events which could
        disrupt traffic.
    :cvar FILM_TVMAKING: Film or TV making event which could disrupt
        traffic.
    :cvar FOOTBALL_MATCH: Football match that could disrupt traffic.
    :cvar FUNFAIR: Periodic (e.g. annual), often traditional, gathering
        for entertainment, which could disrupt traffic.
    :cvar GARDENING_OR_FLOWER_SHOW: Gardening and/or flower show or
        event which could disrupt traffic.
    :cvar GOLF_TOURNAMENT: Golf tournament event that could disrupt
        traffic.
    :cvar HOCKEY_GAME: Hockey game event that could disrupt traffic.
    :cvar HORSE_RACE_MEETING: Horse race meeting that could disrupt
        traffic.
    :cvar INTERNATIONAL_SPORTS_MEETING: Large sporting event of an
        international nature that could disrupt traffic.
    :cvar MAJOR_EVENT: Significant organised event either on or near the
        roadway which could disrupt traffic.
    :cvar MARATHON: Marathon, cross-country or road running event that
        could disrupt traffic.
    :cvar MARKET: Periodic (e.g. weekly) gathering for buying and
        selling, which could disrupt traffic.
    :cvar MATCH: Sports match of unspecified type that could disrupt
        traffic.
    :cvar MOTOR_SHOW: Motor show which could disrupt traffic.
    :cvar MOTOR_SPORT_RACE_MEETING: Motor sport race meeting that could
        disrupt traffic.
    :cvar PARADE: Formal display or organised procession which could
        disrupt traffic.
    :cvar PROCESSION: An organised procession which could disrupt
        traffic.
    :cvar RACE_MEETING: Race meeting (other than horse or motor sport)
        that could disrupt traffic.
    :cvar RUGBY_MATCH: Rugby match that could disrupt traffic.
    :cvar SEVERAL_MAJOR_EVENTS: A series of significant organised events
        either on or near the roadway which could disrupt traffic.
    :cvar SHOW: Entertainment event that could disrupt traffic.
    :cvar SHOW_JUMPING: Horse showing jumping and tournament event that
        could disrupt traffic.
    :cvar SPORTS_MEETING: Sports event of unspecified type that could
        disrupt traffic.
    :cvar STATE_OCCASION: Public ceremony or visit of national or
        international significance which could disrupt traffic.
    :cvar TENNIS_TOURNAMENT: Tennis tournament that could disrupt
        traffic.
    :cvar TOURNAMENT: Sporting event or series of events of unspecified
        type lasting more than one day which could disrupt traffic.
    :cvar TRADE_FAIR: A periodic (e.g. annual), often traditional,
        gathering for trade promotion, which could disrupt traffic.
    :cvar WATER_SPORTS_MEETING: Water sports meeting that could disrupt
        traffic.
    :cvar WINTER_SPORTS_MEETING: Winter sports meeting or event (e.g.
        skiing, ski jumping, skating) that could disrupt traffic.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    AGRICULTURAL_SHOW = "agriculturalShow"
    AIR_SHOW = "airShow"
    ATHLETICS_MEETING = "athleticsMeeting"
    COMMERCIAL_EVENT = "commercialEvent"
    CULTURAL_EVENT = "culturalEvent"
    BALL_GAME = "ballGame"
    BASEBALL_GAME = "baseballGame"
    BASKETBALL_GAME = "basketballGame"
    BICYCLE_RACE = "bicycleRace"
    BOAT_RACE = "boatRace"
    BOAT_SHOW = "boatShow"
    BOXING_TOURNAMENT = "boxingTournament"
    BULL_FIGHT = "bullFight"
    CEREMONIAL_EVENT = "ceremonialEvent"
    CONCERT = "concert"
    CRICKET_MATCH = "cricketMatch"
    EXHIBITION = "exhibition"
    FAIR = "fair"
    FESTIVAL = "festival"
    FILM_TVMAKING = "filmTVMaking"
    FOOTBALL_MATCH = "footballMatch"
    FUNFAIR = "funfair"
    GARDENING_OR_FLOWER_SHOW = "gardeningOrFlowerShow"
    GOLF_TOURNAMENT = "golfTournament"
    HOCKEY_GAME = "hockeyGame"
    HORSE_RACE_MEETING = "horseRaceMeeting"
    INTERNATIONAL_SPORTS_MEETING = "internationalSportsMeeting"
    MAJOR_EVENT = "majorEvent"
    MARATHON = "marathon"
    MARKET = "market"
    MATCH = "match"
    MOTOR_SHOW = "motorShow"
    MOTOR_SPORT_RACE_MEETING = "motorSportRaceMeeting"
    PARADE = "parade"
    PROCESSION = "procession"
    RACE_MEETING = "raceMeeting"
    RUGBY_MATCH = "rugbyMatch"
    SEVERAL_MAJOR_EVENTS = "severalMajorEvents"
    SHOW = "show"
    SHOW_JUMPING = "showJumping"
    SPORTS_MEETING = "sportsMeeting"
    STATE_OCCASION = "stateOccasion"
    TENNIS_TOURNAMENT = "tennisTournament"
    TOURNAMENT = "tournament"
    TRADE_FAIR = "tradeFair"
    WATER_SPORTS_MEETING = "waterSportsMeeting"
    WINTER_SPORTS_MEETING = "winterSportsMeeting"
    OTHER = "other"
