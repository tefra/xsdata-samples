from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


class TimeDataType(Enum):
    """
    TimeDataType restricts SimpleDataType to specify the allowable data
    types for representing a time value.

    :cvar OBSERVATIONAL_TIME_PERIOD: Observational time periods are the
        superset of all time periods in SDMX. It is the union of the
        standard time periods (i.e. Gregorian time periods, the
        reporting time periods, and date time) and a time range.
    :cvar STANDARD_TIME_PERIOD: Standard time periods is a superset of
        distinct time period in SDMX. It is the union of the basic time
        periods (i.e. the Gregorian time periods and date time) and the
        reporting time periods.
    :cvar BASIC_TIME_PERIOD: BasicTimePeriod time periods is a superset
        of the Gregorian time periods and a date time.
    :cvar GREGORIAN_TIME_PERIOD: Gregorian time periods correspond to
        calendar periods and are represented in ISO-8601 formats. This
        is the union of the year, year month, and date formats.
    :cvar GREGORIAN_YEAR: A Gregorian time period corresponding to W3C
        XML Schema's xs:gYear datatype, which is based on ISO-8601.
    :cvar GREGORIAN_YEAR_MONTH: A time datatype corresponding to W3C XML
        Schema's xs:gYearMonth datatype, which is based on ISO-8601.
    :cvar GREGORIAN_DAY: A time datatype corresponding to W3C XML
        Schema's xs:date datatype, which is based on ISO-8601.
    :cvar REPORTING_TIME_PERIOD: Reporting time periods represent
        periods of a standard length within a reporting year, where to
        start of the year (defined as a month and day) must be defined
        elsewhere or it is assumed to be January 1. This is the union of
        the reporting year, semester, trimester, quarter, month, week,
        and day.
    :cvar REPORTING_YEAR: A reporting year represents a period of 1 year
        (P1Y) from the start date of the reporting year. This is
        expressed as using the SDMX specific ReportingYearType.
    :cvar REPORTING_SEMESTER: A reporting semester represents a period
        of 6 months (P6M) from the start date of the reporting year.
        This is expressed as using the SDMX specific
        ReportingSemesterType.
    :cvar REPORTING_TRIMESTER: A reporting trimester represents a period
        of 4 months (P4M) from the start date of the reporting year.
        This is expressed as using the SDMX specific
        ReportingTrimesterType.
    :cvar REPORTING_QUARTER: A reporting quarter represents a period of
        3 months (P3M) from the start date of the reporting year. This
        is expressed as using the SDMX specific ReportingQuarterType.
    :cvar REPORTING_MONTH: A reporting month represents a period of 1
        month (P1M) from the start date of the reporting year. This is
        expressed as using the SDMX specific ReportingMonthType.
    :cvar REPORTING_WEEK: A reporting week represents a period of 7 days
        (P7D) from the start date of the reporting year. This is
        expressed as using the SDMX specific ReportingWeekType.
    :cvar REPORTING_DAY: A reporting day represents a period of 1 day
        (P1D) from the start date of the reporting year. This is
        expressed as using the SDMX specific ReportingDayType.
    :cvar DATE_TIME: A time datatype corresponding to W3C XML Schema's
        xs:dateTime datatype.
    :cvar TIME_RANGE: TimeRange defines a time period by providing a
        distinct start (date or date time) and a duration.
    """

    OBSERVATIONAL_TIME_PERIOD = "ObservationalTimePeriod"
    STANDARD_TIME_PERIOD = "StandardTimePeriod"
    BASIC_TIME_PERIOD = "BasicTimePeriod"
    GREGORIAN_TIME_PERIOD = "GregorianTimePeriod"
    GREGORIAN_YEAR = "GregorianYear"
    GREGORIAN_YEAR_MONTH = "GregorianYearMonth"
    GREGORIAN_DAY = "GregorianDay"
    REPORTING_TIME_PERIOD = "ReportingTimePeriod"
    REPORTING_YEAR = "ReportingYear"
    REPORTING_SEMESTER = "ReportingSemester"
    REPORTING_TRIMESTER = "ReportingTrimester"
    REPORTING_QUARTER = "ReportingQuarter"
    REPORTING_MONTH = "ReportingMonth"
    REPORTING_WEEK = "ReportingWeek"
    REPORTING_DAY = "ReportingDay"
    DATE_TIME = "DateTime"
    TIME_RANGE = "TimeRange"
