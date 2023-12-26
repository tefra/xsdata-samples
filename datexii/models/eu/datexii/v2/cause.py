from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Cause:
    """
    Contains details of the cause of a record within a situation.
    """

    cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "causeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
