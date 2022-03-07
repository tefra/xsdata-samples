from dataclasses import dataclass, field
from typing import Optional
from generali.models.com.generali.enterprise_services.core.gbo.common.headers.v1.base_header_type import BaseHeaderType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/headers/v1"


@dataclass
class QueryResultType(BaseHeaderType):
    """
    <description xmlns="">A header providing meta-data about the result of a
    query.</description>

    :ivar total_count: <description xmlns="">The total number of records
        matched in the query and possibly returned in the payload of the
        response message.</description>
    """
    total_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/headers/v1",
            "required": True,
        }
    )
