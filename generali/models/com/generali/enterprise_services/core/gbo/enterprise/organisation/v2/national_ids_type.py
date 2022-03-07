from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.national_id_type import NationalIdType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass
class NationalIdsType:
    national_id: List[NationalIdType] = field(
        default_factory=list,
        metadata={
            "name": "NationalId",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        }
    )
