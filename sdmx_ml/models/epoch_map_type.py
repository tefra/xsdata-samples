from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.epoch_map_base_type import EpochMapBaseType
from sdmx_ml.models.epoch_period_type import EpochPeriodType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class EpochMapType(EpochMapBaseType):
    base_period: None | str = field(
        default=None,
        metadata={
            "name": "basePeriod",
            "type": "Attribute",
            "required": True,
        },
    )
    epoch_period: None | EpochPeriodType = field(
        default=None,
        metadata={
            "name": "epochPeriod",
            "type": "Attribute",
            "required": True,
        },
    )
