from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Notprsubset:
    class Meta:
        name = "notprsubset"
        namespace = "http://www.w3.org/1998/Math/MathML"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
