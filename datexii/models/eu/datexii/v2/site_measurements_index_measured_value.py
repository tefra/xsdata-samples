from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.measured_value import MeasuredValue

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SiteMeasurementsIndexMeasuredValue:
    class Meta:
        name = "_SiteMeasurementsIndexMeasuredValue"

    measured_value: Optional[MeasuredValue] = field(
        default=None,
        metadata={
            "name": "measuredValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
