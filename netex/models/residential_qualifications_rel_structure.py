from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .residential_qualification import ResidentialQualification
from .residential_qualification_ref import ResidentialQualificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResidentialQualificationsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "residentialQualifications_RelStructure"

    residential_qualification_ref: List[ResidentialQualificationRef] = field(
        default_factory=list,
        metadata={
            "name": "ResidentialQualificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    residential_qualification: List[ResidentialQualification] = field(
        default_factory=list,
        metadata={
            "name": "ResidentialQualification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
