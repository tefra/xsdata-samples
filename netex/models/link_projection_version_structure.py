from __future__ import annotations

from dataclasses import dataclass, field

from .link_ref_structure import LinkRefStructure
from .point_on_link_by_value_structure import PointOnLinkByValueStructure
from .point_on_link_ref_structure_1 import PointOnLinkRefStructure1
from .projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkProjectionVersionStructure(ProjectionVersionStructure):
    class Meta:
        name = "LinkProjection_VersionStructure"

    projected_link_ref: LinkRefStructure | None = field(
        default=None,
        metadata={
            "name": "ProjectedLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    project_to_link_ref: LinkRefStructure | None = field(
        default=None,
        metadata={
            "name": "ProjectToLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_point_on_link_ref_or_start_point_on_link_by_value: (
        PointOnLinkRefStructure1 | PointOnLinkByValueStructure | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartPointOnLinkRef",
                    "type": PointOnLinkRefStructure1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartPointOnLinkByValue",
                    "type": PointOnLinkByValueStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    end_point_on_link_ref_or_end_point_on_link_by_value: (
        PointOnLinkRefStructure1 | PointOnLinkByValueStructure | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndPointOnLinkRef",
                    "type": PointOnLinkRefStructure1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndPointOnLinkByValue",
                    "type": PointOnLinkByValueStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
