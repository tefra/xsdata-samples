from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class OverlineEnd:
    """
    <div> <h3>Overline End</h3> </div>.
    """

    class Meta:
        name = "overline-end"
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
    specific_use: str | None = field(
        default=None,
        metadata={
            "name": "specific-use",
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
