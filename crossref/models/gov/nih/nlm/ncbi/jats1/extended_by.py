from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.xlink.actuate_type import ActuateType
from crossref.models.xlink.show_type import ShowType
from crossref.models.xlink.type_type import TypeType

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class ExtendedBy:
    """
    <div> <h3>Extended-by Model</h3> </div>.
    """

    class Meta:
        name = "extended-by"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    designator: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hreflang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: None | str = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    actuate: None | ActuateType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
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
    show: None | ShowType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
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
