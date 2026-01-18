from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.country_enum import CountryEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.public_holiday_type_enum import (
    PublicHolidayTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PublicHoliday:
    """
    Specification of the public holiday type in a specific country or
    region.

    Use this component only when specialDayType is set to 'publicHoliday'
    or 'holidays'.

    :ivar country: ISO 3166-1 two character country code.
    :ivar country_subdivision: ISO 3166-2 country sub-division code (up
        to 3 characters).
    :ivar region: Region of country (e.g. "Scotland", "Wales" etc. if
        country = GB)
    :ivar public_holiday_type: Specifies the public holiday type for the
        country or region.
    :ivar public_holiday_name: Specification of public holiday, if the
        enumeration values do not fit.
    :ivar public_holiday_extension:
    """

    country: CountryEnum | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    country_subdivision: str | None = field(
        default=None,
        metadata={
            "name": "countrySubdivision",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    region: MultilingualString | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    public_holiday_type: PublicHolidayTypeEnum | None = field(
        default=None,
        metadata={
            "name": "publicHolidayType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    public_holiday_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "publicHolidayName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    public_holiday_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "publicHolidayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
