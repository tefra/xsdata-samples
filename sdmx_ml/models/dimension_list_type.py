from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.dimension import Dimension
from sdmx_ml.models.dimension_list_base_type import DimensionListBaseType
from sdmx_ml.models.time_dimension import TimeDimension

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DimensionListType(DimensionListBaseType):
    """
    DimensionListType describes the key descriptor for a data structure
    definition.

    The order of the declaration of child dimensions is significant: it is
    used to describe the order in which they will appear in data formats
    for which key values are supplied in an ordered fashion (exclusive of
    the time dimension, which is not represented as a member of the ordered
    key). Any data structure definition which uses the time dimension
    should also declare a frequency dimension, conventionally the first
    dimension in the key (the set of ordered non-time dimensions). If is
    not necessary to assign a time dimension, as data can be organised in
    any fashion required.
    """

    dimension: tuple[Dimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
    time_dimension: TimeDimension | None = field(
        default=None,
        metadata={
            "name": "TimeDimension",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
