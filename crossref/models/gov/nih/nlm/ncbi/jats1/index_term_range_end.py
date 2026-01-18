from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class IndexTermRangeEnd:
    """
    <div> <h3>Index Term Range End</h3> </div>.
    """

    class Meta:
        name = "index-term-range-end"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
