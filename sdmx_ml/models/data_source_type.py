from dataclasses import dataclass, field
from typing import Union

from sdmx_ml.models.queryable_data_source_type_2 import (
    QueryableDataSourceType2,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class DataSourceType:
    """
    DataSourceType specifies the properties of a data or metadata source.

    Either a simple data source, a queryable data source, or both must be
    specified.
    """

    simple_data_source_or_queryable_data_source: tuple[
        str | QueryableDataSourceType2, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleDataSource",
                    "type": str,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                    "max_occurs": 2,
                },
                {
                    "name": "QueryableDataSource",
                    "type": QueryableDataSourceType2,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                    "max_occurs": 2,
                },
            ),
            "max_occurs": 2,
        },
    )
