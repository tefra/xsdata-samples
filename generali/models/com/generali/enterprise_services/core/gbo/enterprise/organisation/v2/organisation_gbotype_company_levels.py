from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import CodeType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass
class OrganisationGbotypeCompanyLevels:
    class Meta:
        global_type = False

    company_level: List[CodeType] = field(
        default_factory=list,
        metadata={
            "name": "CompanyLevel",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        }
    )
