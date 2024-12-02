from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.parking_record import ParkingRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingTable:
    """
    A collection of parking records, which can be parking sites or groups of
    parking sites.

    :ivar parking_table_name: The name of the parking table.
    :ivar parking_table_version_time: The date/time that this version of
        the parking table was defined by the supplier. The identity and
        version of the table are defined by the class stereotype
        implementation.
    :ivar parking_record:
    :ivar parking_table_extension:
    :ivar id:
    :ivar version:
    """

    parking_table_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "parkingTableName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_table_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "parkingTableVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_record: list[ParkingRecord] = field(
        default_factory=list,
        metadata={
            "name": "parkingRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    parking_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
