from dataclasses import dataclass, field
from typing import List, Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.collation_algorithm_code_type import CollationAlgorithmCodeType
from generali.models.com.generali.enterprise_services.core.gbo.common.v1.sort_order_code_type import SortOrderCodeType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class SortExpressionType:
    """
    A component holding the specification of the sorting required on the query.

    :ivar path_text: The path by which to sort the result set returned
        from the query.
    :ivar sort_order_code: The direction by which to sort a set of
        values.
    :ivar collation_algorithm_code: The collation (sort) algorithm to
        use in the sorting to the result set
    """
    path_text: List[str] = field(
        default_factory=list,
        metadata={
            "name": "PathText",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "min_occurs": 1,
        }
    )
    sort_order_code: Optional[SortOrderCodeType] = field(
        default=None,
        metadata={
            "name": "sortOrderCode",
            "type": "Attribute",
        }
    )
    collation_algorithm_code: Optional[CollationAlgorithmCodeType] = field(
        default=None,
        metadata={
            "name": "collationAlgorithmCode",
            "type": "Attribute",
        }
    )
