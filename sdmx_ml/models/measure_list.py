from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.measure_list_type import MeasureListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MeasureList(MeasureListType):
    """
    MeasureList describes the measure descriptor for a data structure.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"
        )
