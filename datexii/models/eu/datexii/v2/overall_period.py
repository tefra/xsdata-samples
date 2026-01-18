from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.period import Period

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OverallPeriod:
    """
    A continuous or discontinuous period of validity defined by overall
    bounding start and end times and the possible intersection of valid
    periods (potentially recurring) with the complement of exception
    periods (also potentially recurring).

    :ivar overall_start_time: Start of bounding period of validity
        defined by date and time.
    :ivar overall_end_time: End of bounding period of validity defined
        by date and time.
    :ivar valid_period: A single time period, a recurring time period or
        a set of different recurring time periods during which validity
        is true.
    :ivar exception_period: A single time period, a recurring time
        period or a set of different recurring time periods during which
        validity is false.
    :ivar overall_period_extension:
    """

    overall_start_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "overallStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    overall_end_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "overallEndTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    valid_period: list[Period] = field(
        default_factory=list,
        metadata={
            "name": "validPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    exception_period: list[Period] = field(
        default_factory=list,
        metadata={
            "name": "exceptionPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    overall_period_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "overallPeriodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
