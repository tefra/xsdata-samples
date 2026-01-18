from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.line_of_business_detail_type import (
    LineOfBusinessDetailType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass(kw_only=True)
class LineOfBusinessType:
    line_of_business: LineOfBusinessDetailType = field(
        metadata={
            "name": "LineOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
            "required": True,
        }
    )
    sub_line_of_business: None | LineOfBusinessDetailType = field(
        default=None,
        metadata={
            "name": "SubLineOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1",
        },
    )
