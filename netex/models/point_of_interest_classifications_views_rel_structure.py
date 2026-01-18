from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .point_of_interest_classification_ref import (
    PointOfInterestClassificationRef,
)
from .point_of_interest_classification_view import (
    PointOfInterestClassificationView,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestClassificationsViewsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "pointOfInterestClassificationsViews_RelStructure"

    point_of_interest_classification_ref_or_point_of_interest_classification_view: Iterable[
        PointOfInterestClassificationRef | PointOfInterestClassificationView
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOfInterestClassificationRef",
                    "type": PointOfInterestClassificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestClassificationView",
                    "type": PointOfInterestClassificationView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
