from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.driving_condition_type_enum import (
    DrivingConditionTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class Conditions(TrafficElement):
    """
    Any conditions which have the potential to degrade normal driving
    conditions.

    :ivar driving_condition_type: Description of the driving conditions
        at the specified location.
    :ivar conditions_extension:
    """

    driving_condition_type: None | DrivingConditionTypeEnum = field(
        default=None,
        metadata={
            "name": "drivingConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    conditions_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "conditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
