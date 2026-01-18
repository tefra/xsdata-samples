from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class GivenNames:
    """
    <div> <h3>Given (First) Names</h3> </div>.
    """

    class Meta:
        name = "given-names"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    initials: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: str | None = field(
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
