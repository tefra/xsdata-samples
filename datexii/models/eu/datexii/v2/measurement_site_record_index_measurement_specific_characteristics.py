from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.measurement_specific_characteristics import (
    MeasurementSpecificCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasurementSiteRecordIndexMeasurementSpecificCharacteristics:
    class Meta:
        name = "_MeasurementSiteRecordIndexMeasurementSpecificCharacteristics"

    measurement_specific_characteristics: (
        MeasurementSpecificCharacteristics | None
    ) = field(
        default=None,
        metadata={
            "name": "measurementSpecificCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    index: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
