from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.niso.org/schemas/ali/1.0/"


@dataclass
class LicenseRef:
    """
    <div> <h3>License Reference (Niso Ali)</h3> </div>
    """
    class Meta:
        name = "license_ref"
        namespace = "http://www.niso.org/schemas/ali/1.0/"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
