from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class PageCount:
    """
    <div> <h3>Page Count</h3> </div>.
    """

    class Meta:
        name = "page-count"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    count: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
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
