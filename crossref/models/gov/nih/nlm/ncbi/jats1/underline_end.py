from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class UnderlineEnd:
    """
    <div> <h3>Underline End</h3> </div>.
    """

    class Meta:
        name = "underline-end"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rid: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
