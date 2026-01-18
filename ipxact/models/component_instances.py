from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.component_instance import ComponentInstance

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ComponentInstances:
    """
    Sub instances of internal components.
    """

    class Meta:
        name = "componentInstances"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    component_instance: list[ComponentInstance] = field(
        default_factory=list,
        metadata={
            "name": "componentInstance",
            "type": "Element",
            "min_occurs": 1,
        },
    )
