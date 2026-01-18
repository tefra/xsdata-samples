from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass(kw_only=True)
class OrganisationGbotypeCompanyLevels:
    class Meta:
        global_type = False

    company_level: list[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "CompanyLevel",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
