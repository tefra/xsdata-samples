from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.percentage_value import PercentageValue
from datexii.models.eu.datexii.v2.speed_value import SpeedValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SpeedPercentile:
    """
    Details of percentage (from an observation set) of vehicles whose speeds
    fall below a stated value.

    :ivar vehicle_percentage: The percentage of vehicles from the
        observation set whose speeds fall below the stated speed
        (speedPercentile).
    :ivar speed_percentile: The speed below which the associated
        percentage of vehicles in the measurement set are travelling at.
    :ivar speed_percentile_extension:
    """
    vehicle_percentage: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "vehiclePercentage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    speed_percentile: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    speed_percentile_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedPercentileExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
