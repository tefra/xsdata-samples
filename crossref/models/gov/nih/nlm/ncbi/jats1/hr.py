from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Hr:
    """<div>

    <h3>Horizontal Rule</h3> </div>
    """
    class Meta:
        name = "hr"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
