from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.coverage_type import (
    CoverageType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class CoveragesType:
    coverage: List[CoverageType] = field(
        default_factory=list,
        metadata={
            "name": "Coverage",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
