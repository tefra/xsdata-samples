from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.permit_type_enum import PermitTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingPermit:
    """
    A permission for parking.

    :ivar parking_permit_type: Type of permission for parking.
    :ivar parking_permit_scheme: Scheme of permission for parking.
    :ivar parking_permit_identifier: Identifier of permission for
        parking.
    :ivar parking_permit_extension:
    """

    parking_permit_type: Optional[PermitTypeEnum] = field(
        default=None,
        metadata={
            "name": "parkingPermitType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_permit_scheme: Optional[str] = field(
        default=None,
        metadata={
            "name": "parkingPermitScheme",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    parking_permit_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "parkingPermitIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    parking_permit_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingPermitExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
