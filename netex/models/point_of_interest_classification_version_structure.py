from dataclasses import dataclass, field
from typing import Optional

from .classification_descriptors_rel_structure import (
    ClassificationDescriptorsRelStructure,
)
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationVersionStructure(
    TypeOfValueVersionStructure
):
    class Meta:
        name = "PointOfInterestClassification_VersionStructure"

    alternative_descriptors: ClassificationDescriptorsRelStructure | None = field(
        default=None,
        metadata={
            "name": "alternativeDescriptors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
