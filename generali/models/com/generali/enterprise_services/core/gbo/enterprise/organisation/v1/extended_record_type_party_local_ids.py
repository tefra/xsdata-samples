from dataclasses import dataclass, field
from typing import List
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.party_local_id_type import PartyLocalIdType

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class ExtendedRecordTypePartyLocalIds:
    class Meta:
        global_type = False

    party_local_id: List[PartyLocalIdType] = field(
        default_factory=list,
        metadata={
            "name": "PartyLocalId",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
