from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.time_precision_enum import TimePrecisionEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class BasicData:
    """
    Data that is either measured or calculated (elaborated) at the same
    time or over the same time period.

    :ivar measurement_or_calculation_period: The time elapsed between
        the beginning and the end of the sampling or measurement period.
        This item may differ from the unit attribute; e.g. an hourly
        flow can be estimated from a 5-minute measurement period.
    :ivar measurement_or_calculation_time: Point in time at which this
        specific value or set of values has been measured or calculated.
        It may also be a future time at which a data value is predicted.
    :ivar pertinent_location: The location (e.g. the stretch of road or
        area) to which the data value(s) is or are pertinent/relevant.
        This may be different from the location of the measurement
        equipment (i.e. the measurement site location).
    :ivar basic_data_extension:
    :ivar measurement_or_calculated_time_precision: The precision to
        which the time of measurement or calculation is given.
    """

    measurement_or_calculation_period: float | None = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_or_calculation_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pertinent_location: GroupOfLocations | None = field(
        default=None,
        metadata={
            "name": "pertinentLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    basic_data_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "basicDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    measurement_or_calculated_time_precision: TimePrecisionEnum | None = (
        field(
            default=None,
            metadata={
                "name": "measurementOrCalculatedTimePrecision",
                "type": "Attribute",
            },
        )
    )
