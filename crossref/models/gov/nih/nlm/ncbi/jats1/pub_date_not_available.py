from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class PubDateNotAvailable:
    """
    <div> <h3>Date Not Available Flag</h3> </div>.
    """

    class Meta:
        name = "pub-date-not-available"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

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
