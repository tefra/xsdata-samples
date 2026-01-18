from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class InterfaceType:
    """
    A representation of a component/bus interface relation; i.e. a bus
    interface belonging to a certain component.

    :ivar component_instance_ref: Reference to a component instance
        name.
    :ivar bus_ref: Reference to the components  bus interface
    :ivar id:
    """

    class Meta:
        name = "interfaceType"

    component_instance_ref: str | None = field(
        default=None,
        metadata={
            "name": "componentInstanceRef",
            "type": "Attribute",
            "required": True,
        },
    )
    bus_ref: str | None = field(
        default=None,
        metadata={
            "name": "busRef",
            "type": "Attribute",
            "required": True,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
