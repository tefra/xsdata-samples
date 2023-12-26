from dataclasses import dataclass
from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.query_result_type import (
    QueryResultType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


@dataclass
class QueryResult(QueryResultType):
    """
    <description xmlns="">A header providing meta-data about the result of a
    query.</description>
    """

    class Meta:
        namespace = "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
