from dataclasses import dataclass, field
from typing import List
from npo.models.name_type import NameType
from npo.models.person_type import PersonType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class CreditsType:
    class Meta:
        name = "creditsType"

    person: List[PersonType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "sequence": 316,
        }
    )
    name: List[NameType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "sequence": 316,
        }
    )
