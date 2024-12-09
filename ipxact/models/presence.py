from dataclasses import dataclass, field

from ipxact.models.presence_type import PresenceType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Presence:
    """If this element is present, the existance of the port is controlled by the
    specified value.

    valid values are 'illegal', 'required' and 'optional'.
    """

    class Meta:
        name = "presence"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: PresenceType = field(
        default=PresenceType.OPTIONAL,
        metadata={
            "required": True,
        },
    )
