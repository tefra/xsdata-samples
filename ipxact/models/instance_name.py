from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class InstanceName:
    """
    An instance name assigned to subcomponent instances and contained channels,
    that is unique within the parent component.
    """

    class Meta:
        name = "instanceName"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
