from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication
from datexii.models.eu.datexii.v2.vms_unit_table import VmsUnitTable

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsTablePublication(PayloadPublication):
    """
    A publication containing one or more VMS Unit Tables each comprising a set of
    records which hold details of VMS units.
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
    vms_unit_table: List[VmsUnitTable] = field(
        default_factory=list,
        metadata={
            "name": "vmsUnitTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    vms_table_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
