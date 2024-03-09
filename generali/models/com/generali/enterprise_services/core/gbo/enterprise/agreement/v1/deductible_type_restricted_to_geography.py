from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.geography_type import (
    GeographyType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class DeductibleTypeRestrictedToGeography:
    class Meta:
        global_type = False

    geography: List[GeographyType] = field(
        default_factory=list,
        metadata={
            "name": "Geography",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
