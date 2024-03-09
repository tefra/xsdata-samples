from dataclasses import dataclass

from .point_of_interest_classification_version_structure import (
    PointOfInterestClassificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassification(
    PointOfInterestClassificationVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
