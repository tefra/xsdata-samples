from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.road import Road

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class RoadNode(Road):
    """
    A road node as part of the specialised road identified by the name of a
    junctionon on this road.

    :ivar junction_name: Name of the junction.
    :ivar road_node_extension:
    """

    junction_name: MultilingualString = field(
        metadata={
            "name": "junctionName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    road_node_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "roadNodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
