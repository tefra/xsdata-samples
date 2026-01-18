from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.party_local_id_type import (
    PartyLocalIdType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass(kw_only=True)
class ExtendedRecordTypePartyLocalIds:
    class Meta:
        global_type = False

    party_local_id: list[PartyLocalIdType] = field(
        default_factory=list,
        metadata={
            "name": "PartyLocalId",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
