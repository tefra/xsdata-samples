from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Annotation:
    class Meta:
        name = "annotation"
        namespace = "http://www.w3.org/1998/Math/MathML"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: object | None = field(
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
    cd: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    encoding: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_url: str | None = field(
        default=None,
        metadata={
            "name": "definitionURL",
            "type": "Attribute",
        },
    )
    src: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
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
