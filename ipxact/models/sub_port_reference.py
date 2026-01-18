from dataclasses import dataclass, field

from ipxact.models.part_select import PartSelect

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class SubPortReference:
    """
    :ivar part_select:
    :ivar sub_port_ref: A subPort on the referenced structured port.
    :ivar id:
    """

    class Meta:
        name = "subPortReference"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    part_select: PartSelect | None = field(
        default=None,
        metadata={
            "name": "partSelect",
            "type": "Element",
        },
    )
    sub_port_ref: str | None = field(
        default=None,
        metadata={
            "name": "subPortRef",
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
