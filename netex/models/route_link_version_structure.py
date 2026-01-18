from __future__ import annotations

from dataclasses import dataclass, field

from .link_version_structure import LinkVersionStructure
from .mode_restriction_assessments_rel_structure import (
    ModeRestrictionAssessmentsRelStructure,
)
from .operational_context_ref import OperationalContextRef
from .route_point_ref_structure import RoutePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "RouteLink_VersionStructure"

    from_point_ref: None | RoutePointRefStructure = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to_point_ref: None | RoutePointRefStructure = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    operational_context_ref: None | OperationalContextRef = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mode_restriction_assessments: (
        None | ModeRestrictionAssessmentsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "modeRestrictionAssessments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
