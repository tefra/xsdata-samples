from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TargetElement:
    class Meta:
        name = "targetElement"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )