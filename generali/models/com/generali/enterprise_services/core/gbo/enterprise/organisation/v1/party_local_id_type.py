from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class PartyLocalIdType:
    id: str | None = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "required": True,
        },
    )
    sender: str | None = field(
        default=None,
        metadata={
            "name": "Sender",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "required": True,
        },
    )
    party_type: str | None = field(
        default=None,
        metadata={
            "name": "PartyType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "required": True,
        },
    )
