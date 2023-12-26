from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication
from datexii.models.eu.datexii.v2.traffic_view import TrafficView

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TrafficViewPublication(PayloadPublication):
    """
    A publication containing one or more traffic views.
    """

    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    traffic_view: List[TrafficView] = field(
        default_factory=list,
        metadata={
            "name": "trafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    traffic_view_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
