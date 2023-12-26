from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication
from datexii.models.eu.datexii.v2.vms_unit import VmsUnit

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsPublication(PayloadPublication):
    """
    A publication containing the current status and settings of one or more VMS
    units, each unit controlling one or more individual variable message signs.
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
    vms_unit: List[VmsUnit] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    vms_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
