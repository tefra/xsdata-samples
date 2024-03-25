from dataclasses import dataclass

from sdmx_ml.models.measure_list_type import MeasureListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MeasureList(MeasureListType):
    """
    MeasureList describes the measure descriptor for a data structure.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
