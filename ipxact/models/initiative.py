from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.initiative_type import InitiativeType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Initiative:
    """
    If this element is present, the type of access is restricted to the specified
    value.
    """

    class Meta:
        name = "initiative"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: Optional[InitiativeType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
