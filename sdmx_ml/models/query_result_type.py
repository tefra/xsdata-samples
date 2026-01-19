from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from sdmx_ml.models.result_type import ResultType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry"


@dataclass(frozen=True, kw_only=True)
class QueryResultType:
    """
    QueryResultType describes the structure of a query result for a single
    data source.

    Either a data result or metadata result is detailed, depending on the
    data source.

    :ivar data_result_or_metadata_result:
    :ivar time_series_match: The timeSeriesMatch attribute is true when
        the result is an exact match with the key found in the registry
        - that is, when the registered data source provides a matching
        key. It is set to false when the data source is registered with
        cube-region constraints, or in any other circumstance when it
        cannot be established that the sought-for keys have been exactly
        matched. This is always true when the resulting data source is
        the source of a metadata set.
    """

    data_result_or_metadata_result: (
        None | QueryResultType.DataResult | QueryResultType.MetadataResult
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DataResult",
                    "type": ForwardRef("QueryResultType.DataResult"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry",
                },
                {
                    "name": "MetadataResult",
                    "type": ForwardRef("QueryResultType.MetadataResult"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry",
                },
            ),
        },
    )
    time_series_match: bool = field(
        metadata={
            "name": "timeSeriesMatch",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(frozen=True, kw_only=True)
    class DataResult(ResultType):
        pass

    @dataclass(frozen=True, kw_only=True)
    class MetadataResult(ResultType):
        pass
