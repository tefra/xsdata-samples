from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.limit_type import (
    LimitType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass(kw_only=True)
class CyberExclusionType:
    excluded: None | bool = field(
        default=None,
        metadata={
            "name": "Excluded",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    cover_type: None | str = field(
        default=None,
        metadata={
            "name": "CoverType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    limit: None | LimitType = field(
        default=None,
        metadata={
            "name": "Limit",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
