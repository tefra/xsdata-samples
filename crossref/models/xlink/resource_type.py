from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.xlink.type_type import TypeType

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


@dataclass(kw_only=True)
class ResourceType:
    class Meta:
        name = "resourceType"

    type_value: TypeType = field(
        init=False,
        default=TypeType.RESOURCE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        },
    )
    role: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    label: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
