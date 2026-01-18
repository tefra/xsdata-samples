from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.reference_source_type import (
    ReferenceSourceType,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


@dataclass
class OrganisationReferenceTypeSender(CodeType):
    class Meta:
        global_type = False

    reference_type: None | ReferenceSourceType = field(
        default=None,
        metadata={
            "name": "referenceType",
            "type": "Attribute",
        },
    )
