from dataclasses import dataclass, field

from sdmx_ml.models.queryable_data_source_type_1 import (
    QueryableDataSourceType1,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class QueryableDataSourceType2(QueryableDataSourceType1):
    """
    QueryableDataSourceType describes a queryable data source, and add a fixed
    attribute for ensuring only one queryable source can be provided.

    :ivar type_value: TYPE is a fixed attribute that is used to ensure
        only one queryable data source may be provided, when it is
        referenced in a uniqueness constraint.
    """

    class Meta:
        name = "QueryableDataSourceType"

    type_value: str = field(
        init=False,
        default="QUERY",
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        },
    )
