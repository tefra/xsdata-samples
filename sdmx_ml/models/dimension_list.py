from dataclasses import dataclass

from sdmx_ml.models.dimension_list_type import DimensionListType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DimensionList(DimensionListType):
    """DimensionList describes the key descriptor for the data structure
    definition.

    It is an ordered set of metadata concepts that, combined, classify a
    statistical series, such as a time series, and whose values, when
    combined (the key) in an instance such as a data set, uniquely
    identify a specific series.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
