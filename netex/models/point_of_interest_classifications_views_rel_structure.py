from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .point_of_interest_classification_ref import PointOfInterestClassificationRef
from .point_of_interest_classification_view import PointOfInterestClassificationView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationsViewsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "pointOfInterestClassificationsViews_RelStructure"

    point_of_interest_classification_ref: List[PointOfInterestClassificationRef] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    point_of_interest_classification_view: List[PointOfInterestClassificationView] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
