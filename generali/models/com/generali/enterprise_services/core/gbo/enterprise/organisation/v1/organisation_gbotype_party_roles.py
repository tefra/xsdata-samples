from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class OrganisationGbotypePartyRoles:
    class Meta:
        global_type = False

    role: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
