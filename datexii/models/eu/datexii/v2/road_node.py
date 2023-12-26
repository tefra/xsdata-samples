from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.road import Road

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class RoadNode(Road):
    """
    A road node as part of the specialised road identified by the name of a
    junctionon on this road.

    :ivar junction_name: Name of the junction.
    :ivar road_node_extension:
    """

    junction_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "junctionName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    road_node_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadNodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
