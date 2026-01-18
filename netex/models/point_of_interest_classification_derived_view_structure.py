from dataclasses import dataclass, field

from .derived_view_structure import DerivedViewStructure
from .multilingual_string import MultilingualString
from .point_of_interest_classification_ref import (
    PointOfInterestClassificationRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "PointOfInterestClassification_DerivedViewStructure"

    point_of_interest_classification_ref: (
        PointOfInterestClassificationRef | None
    ) = field(
        default=None,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
