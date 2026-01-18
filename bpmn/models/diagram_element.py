from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.omg.org/spec/DD/20100524/DI"


@dataclass(kw_only=True)
class DiagramElement:
    class Meta:
        namespace = "http://www.omg.org/spec/DD/20100524/DI"

    extension: None | DiagramElement.Extension = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )

    @dataclass(kw_only=True)
    class Extension:
        other_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            },
        )
