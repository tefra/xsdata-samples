from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class HolidayTypeEnumeration(Enum):
    ANY_DAY = "AnyDay"
    WORKING_DAY = "WorkingDay"
    SCHOOL_DAY = "SchoolDay"
    NOT_HOLIDAY = "NotHoliday"
    NOT_WORKING_DAY = "NotWorkingDay"
    NOT_SCHOOL_DAY = "NotSchoolDay"
    ANY_HOLIDAY = "AnyHoliday"
    LOCAL_HOLIDAY = "LocalHoliday"
    REGIONAL_HOLIDAY = "RegionalHoliday"
    NATIONAL_HOLIDAY = "NationalHoliday"
    HOLIDAY_DISPLACEMENT_DAY = "HolidayDisplacementDay"
    EVE_OF_HOLIDAY = "EveOfHoliday"
