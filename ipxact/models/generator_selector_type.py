from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.group_selector import GroupSelector

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class GeneratorSelectorType:
    class Meta:
        name = "generatorSelectorType"

    group_selector: GroupSelector = field(
        metadata={
            "name": "groupSelector",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
