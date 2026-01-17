from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.read_action_type import ReadActionType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ReadAction:
    """
    A list of possible actions for a read to set the field after the read.
    'clear' means that after a read the field is cleared. 'set' means that
    after a read the field is set. 'modify' means after a read the field is
    modified.

    If not present the field value is not modified after a read.
    """

    class Meta:
        name = "readAction"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: Optional[ReadActionType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    modify: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
