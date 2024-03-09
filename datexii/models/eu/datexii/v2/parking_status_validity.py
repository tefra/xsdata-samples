from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.overall_period import OverallPeriod

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingStatusValidity:
    """To be used only for historical or forecasted data.

    Choose between an explicit point of time, an offset or all points of
    time within a specified period.

    :ivar parking_status_time: Only use for forecasts or historical data
        to express the point of time for which the information of this
        parking is either reported or forecasted. Alternately you can
        define this point of time as an offset with
        'parkingStatusTimeOffsetToOrigin'.
    :ivar parking_status_time_offset_to_origin: Only use for forecasts
        or historical data to express the point of time for which the
        information of this parking is either reported or forecasted (in
        form of an offset in seconds to 'parkingStatusOriginTime'; use
        negative values for historical data).
    :ivar validity_time_specification: A specification of periods of
        validity defined by overall bounding start and end times and the
        possible intersection of valid periods with exception periods
        (exception periods overriding valid periods).
    :ivar parking_status_validity_extension:
    """

    parking_status_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "parkingStatusTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_status_time_offset_to_origin: Optional[float] = field(
        default=None,
        metadata={
            "name": "parkingStatusTimeOffsetToOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    validity_time_specification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_status_validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingStatusValidityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
