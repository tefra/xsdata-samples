from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


class SimpleDataType(Enum):
    """
    SimpleDataType restricts BasicComponentDataType to specify the
    allowable data types for a data structure definition component.

    The XHTML representation is removed as a possible type.

    :cvar STRING: A string datatype corresponding to W3C XML Schema's
        xs:string datatype.
    :cvar ALPHA: A string datatype which only allows for the simple
        alphabetic character set of A-Z, a-z.
    :cvar ALPHA_NUMERIC: A string datatype which only allows for the
        simple alphabetic character set of A-Z, a-z plus the simple
        numeric character set of 0-9.
    :cvar NUMERIC: A string datatype which only allows for the simple
        numeric character set of 0-9. This format is not treated as an
        integer, and therefore can having leading zeros.
    :cvar BIG_INTEGER: An integer datatype corresponding to W3C XML
        Schema's xs:integer datatype.
    :cvar INTEGER: An integer datatype corresponding to W3C XML Schema's
        xs:int datatype.
    :cvar LONG: A numeric datatype corresponding to W3C XML Schema's
        xs:long datatype.
    :cvar SHORT: A numeric datatype corresponding to W3C XML Schema's
        xs:short datatype.
    :cvar DECIMAL: A numeric datatype corresponding to W3C XML Schema's
        xs:decimal datatype.
    :cvar FLOAT: A numeric datatype corresponding to W3C XML Schema's
        xs:float datatype.
    :cvar DOUBLE: A numeric datatype corresponding to W3C XML Schema's
        xs:double datatype.
    :cvar BOOLEAN: A datatype corresponding to W3C XML Schema's
        xs:boolean datatype.
    :cvar URI: A datatype corresponding to W3C XML Schema's xs:anyURI
        datatype.
    :cvar COUNT: A simple incrementing Integer type. The isSequence
        facet must be set to true, and the interval facet must be set to
        "1".
    :cvar INCLUSIVE_VALUE_RANGE: This value indicates that the
        startValue and endValue attributes provide the inclusive
        boundaries of a numeric range of type xs:decimal.
    :cvar EXCLUSIVE_VALUE_RANGE: This value indicates that the
        startValue and endValue attributes provide the exclusive
        boundaries of a numeric range, of type xs:decimal.
    :cvar INCREMENTAL: This value indicates that the value increments
        according to the value provided in the interval facet, and has a
        true value for the isSequence facet.
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
    :cvar MONTH: A time datatype corresponding to W3C XML Schema's
        xs:gMonth datatype.
    :cvar MONTH_DAY: A time datatype corresponding to W3C XML Schema's
        xs:gMonthDay datatype.
    :cvar DAY: A time datatype corresponding to W3C XML Schema's xs:gDay
        datatype.
    :cvar TIME: A time datatype corresponding to W3C XML Schema's
        xs:time datatype.
    :cvar DURATION: A time datatype corresponding to W3C XML Schema's
        xs:duration datatype.
    :cvar GEOSPATIAL_INFORMATION: A string used to describe geographical
        features like points (e.g., locations of places, landmarks,
        buildings, etc.), lines (e.g., rivers, roads, streets, etc.), or
        areas (e.g., geographical regions, countries, islands, land
        lots, etc.). A mix of different features is possible too, e.g.,
        combining polygons and geographical points to describe a country
        and the location of its capital.
    """

    STRING = "String"
    ALPHA = "Alpha"
    ALPHA_NUMERIC = "AlphaNumeric"
    NUMERIC = "Numeric"
    BIG_INTEGER = "BigInteger"
    INTEGER = "Integer"
    LONG = "Long"
    SHORT = "Short"
    DECIMAL = "Decimal"
    FLOAT = "Float"
    DOUBLE = "Double"
    BOOLEAN = "Boolean"
    URI = "URI"
    COUNT = "Count"
    INCLUSIVE_VALUE_RANGE = "InclusiveValueRange"
    EXCLUSIVE_VALUE_RANGE = "ExclusiveValueRange"
    INCREMENTAL = "Incremental"
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
    MONTH = "Month"
    MONTH_DAY = "MonthDay"
    DAY = "Day"
    TIME = "Time"
    DURATION = "Duration"
    GEOSPATIAL_INFORMATION = "GeospatialInformation"
