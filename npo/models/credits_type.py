from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.name_type import NameType
from npo.models.person_type import PersonType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class CreditsType:
    class Meta:
        name = "creditsType"

    person: list[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    name: list[NameType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
