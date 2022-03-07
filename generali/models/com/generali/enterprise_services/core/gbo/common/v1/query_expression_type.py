from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.logical_operator_code_type import LogicalOperatorCodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.value_expression_type import ValueExpressionType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class QueryExpressionType:
    """
    <description xmlns="">A query expression that allows complex queries to be
    formulated out of a series of value expressions (criteria).</description>

    :ivar value_expression: <description xmlns="">The value to be
        matched in a query criteria. The repeating structure allows more
        than one value to be specified, these must be taken as an
        implict OR function, i.e. This Value-1 OR Value-2 OR
        Value-3.</description>
    :ivar logical_operator_code: <description xmlns="">A field
        indicating how consecutive query expression should be evaluated,
        e.g. Condition-1 AND Condition-2.</description>
    :ivar negation_indicator: <description xmlns="">An indicator of
        whether the query expression should have a NOT applied to it,
        i.e. does NOT equal or is NOT less than.</description>
    """
    value_expression: List[ValueExpressionType] = field(
        default_factory=list,
        metadata={
            "name": "ValueExpression",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    logical_operator_code: Optional[LogicalOperatorCodeType] = field(
        default=None,
        metadata={
            "name": "logicalOperatorCode",
            "type": "Attribute",
        }
    )
    negation_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "negationIndicator",
            "type": "Attribute",
        }
    )
