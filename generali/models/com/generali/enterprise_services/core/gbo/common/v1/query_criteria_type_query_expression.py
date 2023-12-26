from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.query_expression_type import (
    QueryExpressionType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.value_expression_type import (
    ValueExpressionType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class QueryCriteriaTypeQueryExpression:
    """
    :ivar value_expression: <description xmlns="">The value to be
        matched in a query criteria. The repeating structure allows more
        than one value to be specified, these must be taken as an
        implict OR function, i.e. This Value-1 OR Value-2 OR
        Value-3.</description>
    :ivar query_expression: <description xmlns="">A query expression
        that allows complex queries to be formulated out of a series of
        value expressions (criteria).</description>
    """

    class Meta:
        global_type = False

    value_expression: List[ValueExpressionType] = field(
        default_factory=list,
        metadata={
            "name": "ValueExpression",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    query_expression: Optional[QueryExpressionType] = field(
        default=None,
        metadata={
            "name": "QueryExpression",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
