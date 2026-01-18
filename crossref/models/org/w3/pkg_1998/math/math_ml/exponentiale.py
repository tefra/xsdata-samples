from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Exponentiale:
    class Meta:
        name = "exponentiale"
        namespace = "http://www.w3.org/1998/Math/MathML"

    any_element: object | None = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
