from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.permit_type_enum import PermitTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ParkingPermit:
    """
    A permission for parking.

    :ivar parking_permit_type: Type of permission for parking.
    :ivar parking_permit_scheme: Scheme of permission for parking.
    :ivar parking_permit_identifier: Identifier of permission for
        parking.
    :ivar parking_permit_extension:
    """

    parking_permit_type: PermitTypeEnum = field(
        metadata={
            "name": "parkingPermitType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_permit_scheme: None | str = field(
        default=None,
        metadata={
            "name": "parkingPermitScheme",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    parking_permit_identifier: None | str = field(
        default=None,
        metadata={
            "name": "parkingPermitIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    parking_permit_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "parkingPermitExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
