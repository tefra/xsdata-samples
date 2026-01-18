from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class IndexTermRangeEnd:
    """
    <div> <h3>Index Term Range End</h3> </div>.
    """

    class Meta:
        name = "index-term-range-end"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
