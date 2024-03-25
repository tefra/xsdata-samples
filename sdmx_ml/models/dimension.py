from dataclasses import dataclass

from sdmx_ml.models.dimension_type import DimensionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class Dimension(DimensionType):
    """
    Dimension describes the structure of a dimension, which is defined as a
    statistical concept used (most probably together with other statistical
    concepts) to identify a statistical series, such as a time series, e.g. a
    statistical concept indicating certain economic activity or a geographical
    reference area.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
