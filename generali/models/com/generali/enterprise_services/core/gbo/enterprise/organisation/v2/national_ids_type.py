from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.national_id_type import (
    NationalIdType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass(kw_only=True)
class NationalIdsType:
    national_id: list[NationalIdType] = field(
        default_factory=list,
        metadata={
            "name": "NationalId",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
