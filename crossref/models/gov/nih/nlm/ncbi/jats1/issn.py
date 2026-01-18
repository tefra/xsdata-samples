from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class Issn:
    """
    <div> <h3>Issn</h3> </div>.
    """

    class Meta:
        name = "issn"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    pub_type: None | str = field(
        default=None,
        metadata={
            "name": "pub-type",
            "type": "Attribute",
        },
    )
    publication_format: None | str = field(
        default=None,
        metadata={
            "name": "publication-format",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
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
