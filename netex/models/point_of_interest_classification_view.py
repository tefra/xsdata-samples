from dataclasses import dataclass
from .point_of_interest_classification_derived_view_structure import (
    PointOfInterestClassificationDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationView(
    PointOfInterestClassificationDerivedViewStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
