from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Group:
    """Indicates which system interface is being mirrored.

    Name must match a group name present on one or more ports in the
    corresonding bus definition.
    """

    class Meta:
        name = "group"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
