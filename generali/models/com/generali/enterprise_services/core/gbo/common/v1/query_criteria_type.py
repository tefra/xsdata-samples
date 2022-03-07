from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.query_algorithm_code_type import QueryAlgorithmCodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.query_expression_type import QueryExpressionType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.value_expression_type import ValueExpressionType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class QueryCriteriaType:
    """
    :ivar query_expression: <description xmlns="">A query expression
        that allows complex queries to be formulated out of a series of
        value expressions (criteria).</description>
    :ivar start_index: <description xmlns="">A field that supports the
        specification of pagination by a requester. The start index
        indicates the number of the instance matching the query criteria
        from which the page to be returned starts.</description>
    :ivar index_per_page: <description xmlns="">A field that supports
        the specification of the size of the page to be returned in a
        query.</description>
    :ivar matching_algorithm: <description xmlns="">An optional
        indicator of either the strength of matching or the specific
        algorithm to use in matching the records on the server. The
        default is Strict, i.e. match strings exactly.</description>
    """
    query_expression: Optional["QueryCriteriaType.QueryExpression"] = field(
        default=None,
        metadata={
            "name": "QueryExpression",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        }
    )
    start_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "startIndex",
            "type": "Attribute",
        }
    )
    index_per_page: Optional[int] = field(
        default=None,
        metadata={
            "name": "indexPerPage",
            "type": "Attribute",
        }
    )
    matching_algorithm: Optional[QueryAlgorithmCodeType] = field(
        default=None,
        metadata={
            "name": "matchingAlgorithm",
            "type": "Attribute",
        }
    )

    @dataclass
    class QueryExpression:
        """
        :ivar value_expression: <description xmlns="">The value to be
            matched in a query criteria. The repeating structure allows
            more than one value to be specified, these must be taken as
            an implict OR function, i.e. This Value-1 OR Value-2 OR
            Value-3.</description>
        :ivar query_expression: <description xmlns="">A query expression
            that allows complex queries to be formulated out of a series
            of value expressions (criteria).</description>
        """
        value_expression: List[ValueExpressionType] = field(
            default_factory=list,
            metadata={
                "name": "ValueExpression",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )
        query_expression: Optional[QueryExpressionType] = field(
            default=None,
            metadata={
                "name": "QueryExpression",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            }
        )
