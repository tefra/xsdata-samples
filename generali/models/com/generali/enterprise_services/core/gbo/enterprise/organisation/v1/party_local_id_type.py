from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass(kw_only=True)
class PartyLocalIdType:
    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "required": True,
        }
    )
    sender: str = field(
        metadata={
            "name": "Sender",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "required": True,
        }
    )
    party_type: str = field(
        metadata={
            "name": "PartyType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "required": True,
        }
    )
