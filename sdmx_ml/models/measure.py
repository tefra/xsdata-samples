from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.measure_type import MeasureType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class Measure(MeasureType):
    """
    Measure defines the structure of a measure, which is the concept that
    is the value of the phenomenon to be measured in a data set.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"
        )
