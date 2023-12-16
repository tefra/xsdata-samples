from dataclasses import dataclass, field
from typing import List, Union
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .residential_qualification import ResidentialQualification
from .residential_qualification_ref import ResidentialQualificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResidentialQualificationsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "residentialQualifications_RelStructure"

    residential_qualification_ref_or_residential_qualification: List[Union[ResidentialQualificationRef, ResidentialQualification]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationRef",
                    "type": ResidentialQualificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResidentialQualification",
                    "type": ResidentialQualification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
