from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


@dataclass
class XrefFaces:
    class Meta:
        name = "xrefFaces"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "u",
                    "type": ForwardRef("U"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "ovl",
                    "type": ForwardRef("Ovl"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "scp",
                    "type": ForwardRef("Scp"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
                {
                    "name": "font",
                    "type": ForwardRef("Font"),
                    "namespace": "http://www.crossref.org/relations.xsd",
                },
            ),
        },
    )


@dataclass
class B(XrefFaces):
    class Meta:
        name = "b"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class Em(XrefFaces):
    class Meta:
        name = "em"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class Font(XrefFaces):
    class Meta:
        name = "font"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class I(XrefFaces):
    class Meta:
        name = "i"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class Ovl(XrefFaces):
    class Meta:
        name = "ovl"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class Scp(XrefFaces):
    class Meta:
        name = "scp"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class Strong(XrefFaces):
    class Meta:
        name = "strong"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class Sub(XrefFaces):
    class Meta:
        name = "sub"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class Sup(XrefFaces):
    class Meta:
        name = "sup"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class Tt(XrefFaces):
    class Meta:
        name = "tt"
        namespace = "http://www.crossref.org/relations.xsd"


@dataclass
class U(XrefFaces):
    class Meta:
        name = "u"
        namespace = "http://www.crossref.org/relations.xsd"
