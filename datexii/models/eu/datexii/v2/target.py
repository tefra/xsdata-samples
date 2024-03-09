from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Target:
    """
    The details of a DATEX II target client.

    :ivar address: The IP address of a DATEX II target client.
    :ivar protocol: The exchange protocol used between the supplier and
        the client.
    :ivar target_extension:
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    target_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "targetExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
