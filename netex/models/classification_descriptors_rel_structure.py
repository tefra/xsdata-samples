from dataclasses import dataclass, field
from typing import List
from .classification_descriptor_version_structure import (
    ClassificationDescriptorVersionStructure,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassificationDescriptorsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "classificationDescriptors_RelStructure"

    classification_descriptor: List[
        ClassificationDescriptorVersionStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "ClassificationDescriptor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
