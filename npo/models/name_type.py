from dataclasses import dataclass, field
from typing import List, Optional
from npo.models.gtaa_status_type import GtaaStatusType
from npo.models.role_type import RoleType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class NameType:
    class Meta:
        name = "nameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    gtaa_status: Optional[GtaaStatusType] = field(
        default=None,
        metadata={
            "name": "gtaaStatus",
            "type": "Attribute",
        }
    )
