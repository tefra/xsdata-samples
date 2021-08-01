from dataclasses import dataclass, field
from typing import Optional
from npo.models.gtaa_status_type import GtaaStatusType
from npo.models.role_type import RoleType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class PersonType:
    class Meta:
        name = "personType"

    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
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
