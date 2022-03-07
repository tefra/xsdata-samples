from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.base_identified_component_type import BaseIdentifiedComponentType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.query_criteria_type import QueryCriteriaType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.sort_expression_type import SortExpressionType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class QueryType:
    """
    <description xmlns="">A data object that allows simple and complex query
    criteria to be specified against which a set of business objects can be
    matched.</description>

    :ivar identification: <description xmlns="">A component within the
        query that specifies a specific instance of a business to
        retrieve. The ID specified represents the primary key of the
        business object as configured through the
        IDs/ID[/@schemeName=''] field.</description>
    :ivar criteria:
    :ivar sort_expression: A component holding the specification of the
        sorting required on the query.
    :ivar business_object: <description xmlns="">If the Query object is
        being used as a generic query capability then this attribute
        indicates the VBO being searched on. If the query is on a
        specific VBS then it should not be present. If present and
        different from the VBO then it must be ignored.</description>
    """
    identification: Optional[BaseIdentifiedComponentType] = field(
        default=None,
        metadata={
            "name": "Identification",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    criteria: Optional[QueryCriteriaType] = field(
        default=None,
        metadata={
            "name": "Criteria",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    sort_expression: Optional[SortExpressionType] = field(
        default=None,
        metadata={
            "name": "SortExpression",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        }
    )
    business_object: Optional[str] = field(
        default=None,
        metadata={
            "name": "businessObject",
            "type": "Attribute",
        }
    )
