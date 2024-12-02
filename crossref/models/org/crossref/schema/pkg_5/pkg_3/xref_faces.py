from dataclasses import dataclass, field
from typing import ForwardRef

from crossref.models.org.w3.pkg_1998.math.math_ml.math import Math

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


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
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "u",
                    "type": ForwardRef("U"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "ovl",
                    "type": ForwardRef("Ovl"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "scp",
                    "type": ForwardRef("Scp"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "font",
                    "type": ForwardRef("Font"),
                    "namespace": "http://www.crossref.org/schema/5.3.1",
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
            ),
        },
    )


@dataclass
class B(XrefFaces):
    class Meta:
        name = "b"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Em(XrefFaces):
    class Meta:
        name = "em"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Font(XrefFaces):
    class Meta:
        name = "font"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class I(XrefFaces):
    class Meta:
        name = "i"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Ovl(XrefFaces):
    class Meta:
        name = "ovl"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Scp(XrefFaces):
    class Meta:
        name = "scp"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Strong(XrefFaces):
    class Meta:
        name = "strong"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Sub(XrefFaces):
    class Meta:
        name = "sub"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Sup(XrefFaces):
    class Meta:
        name = "sup"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Tt(XrefFaces):
    class Meta:
        name = "tt"
        namespace = "http://www.crossref.org/schema/5.3.1"


@dataclass
class U(XrefFaces):
    class Meta:
        name = "u"
        namespace = "http://www.crossref.org/schema/5.3.1"
