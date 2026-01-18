from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.carriageway_enum import CarriagewayEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.lane_enum import LaneEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class AffectedCarriagewayAndLanes:
    """
    Supplementary positional information which details carriageway and lane
    locations.

    Several instances may exist where the element being described extends
    over more than one carriageway.

    :ivar carriageway: Indicates the section of carriageway to which the
        location relates.
    :ivar lane: Indicates the specific lane to which the location
        relates.
    :ivar footpath: Indicates whether the pedestrian footpath is the
        subject or part of the subject of the location. (True = footpath
        is subject)
    :ivar length_affected: This indicates the length of road measured in
        metres affected by the associated traffic element.
    :ivar affected_carriageway_and_lanes_extension:
    """

    carriageway: CarriagewayEnum = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    lane: list[LaneEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    footpath: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    length_affected: None | float = field(
        default=None,
        metadata={
            "name": "lengthAffected",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    affected_carriageway_and_lanes_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "affectedCarriagewayAndLanesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
