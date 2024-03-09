from dataclasses import dataclass, field
from typing import List

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.contact_involvement import (
    ContactInvolvement,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class ContactsInvolvement:
    contact: List[ContactInvolvement] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
