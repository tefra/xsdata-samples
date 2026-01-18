from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_variance_indicator import TypeVarianceIndicator
from travelport.models.type_variance_type import TypeVarianceType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Variance:
    """
    Indicates any variance in the requested flight.

    Parameters
    ----------
    type_value
        Indicates type Variance, i.e. Actual, Estimated, Canceled and
        Diversion.
    time
        Indicates time for Variance.
    indicator
        Indicates VAriance Indicator, i.e. Early, Late.
    reason
        Reason for Variance
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: TypeVarianceType = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    time: None | str = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
        },
    )
    indicator: None | TypeVarianceIndicator = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        },
    )
    reason: None | str = field(
        default=None,
        metadata={
            "name": "Reason",
            "type": "Attribute",
        },
    )
