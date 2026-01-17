from dataclasses import dataclass, field
from typing import Union

from sdmx_ml.models.cube_key_value_type import CubeKeyValueType
from sdmx_ml.models.member_selection_type import MemberSelectionType
from sdmx_ml.models.time_range_value_type import TimeRangeValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CubeRegionKeyType(MemberSelectionType):
    """
    CubeRegionKeyType is a type for providing a set of values for a
    dimension for the purpose of defining a data cube region.

    A set of distinct value can be provided, or if this dimension is
    represented as time, and time range can be specified.
    """

    value_or_time_range: tuple[
        Union[CubeKeyValueType, TimeRangeValueType], ...
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Value",
                    "type": CubeKeyValueType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "TimeRange",
                    "type": TimeRangeValueType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
