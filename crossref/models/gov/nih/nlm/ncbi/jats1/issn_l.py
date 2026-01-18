from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class IssnL:
    """
    <div> <h3>Issn Linking</h3> </div>.
    """

    class Meta:
        name = "issn-l"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
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
