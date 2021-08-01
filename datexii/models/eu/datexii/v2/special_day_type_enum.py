from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class SpecialDayTypeEnum(Enum):
    """
    Collection of general types of days.

    :cvar BICYCLE_RACE_DAY: Day of local bicycle race.
    :cvar BULL_FIGHT_DAY: Day of local bullfight.
    :cvar CARNIVAL_DAY: Day of a local carnival involving a procession
        along roads.
    :cvar EXHIBITION_DAY: Day of a local exhibition.
    :cvar FESTIVAL_DAY: Day of a local festival.
    :cvar GAMES_DAY: Day of local games (e.g. highland games in
        Scotland).
    :cvar HORSE_RACE_MEETING_DAY: Day of a local horse race meeting.
    :cvar HUNT_MEETING_DAY: Day of a local hunt meeting.
    :cvar MARATHON_RACE_DAY: Day of local marathon race.
    :cvar MARKET_DAY: Day of a local market.
    :cvar MOTOR_SPORT_RACE_MEETING_DAY: Day of a local motor sport race
        meeting.
    :cvar NON_WORKING_DAY: A non-working day in the specific
        country/region.
    :cvar RACE_MEETING_DAY: Day of a local race meeting (other than
        horse or motor sport).
    :cvar REGATTA_DAY: Day of a local regatta.
    :cvar SHOW_DAY: Day of a local show.
    :cvar SPORTS_MEETING_DAY: Day of a local sports meeting.
    :cvar WORKING_DAY: A working day in the specific country/region.
    :cvar SCHOOL_DAY: School day.
    :cvar ELECTION_DAY: Election day.
    :cvar PUBLIC_HOLIDAY: Public holiday.
    :cvar HOLIDAYS: A day within the school holidays. You can use the
        PublicHoliday class to specify more details.
    :cvar UNDEFINED_DAY_TYPE: UndefinedDayType
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    BICYCLE_RACE_DAY = "bicycleRaceDay"
    BULL_FIGHT_DAY = "bullFightDay"
    CARNIVAL_DAY = "carnivalDay"
    EXHIBITION_DAY = "exhibitionDay"
    FESTIVAL_DAY = "festivalDay"
    GAMES_DAY = "gamesDay"
    HORSE_RACE_MEETING_DAY = "horseRaceMeetingDay"
    HUNT_MEETING_DAY = "huntMeetingDay"
    MARATHON_RACE_DAY = "marathonRaceDay"
    MARKET_DAY = "marketDay"
    MOTOR_SPORT_RACE_MEETING_DAY = "motorSportRaceMeetingDay"
    NON_WORKING_DAY = "nonWorkingDay"
    RACE_MEETING_DAY = "raceMeetingDay"
    REGATTA_DAY = "regattaDay"
    SHOW_DAY = "showDay"
    SPORTS_MEETING_DAY = "sportsMeetingDay"
    WORKING_DAY = "workingDay"
    SCHOOL_DAY = "schoolDay"
    ELECTION_DAY = "electionDay"
    PUBLIC_HOLIDAY = "publicHoliday"
    HOLIDAYS = "holidays"
    UNDEFINED_DAY_TYPE = "undefinedDayType"
    UNKNOWN = "unknown"
    OTHER = "other"
