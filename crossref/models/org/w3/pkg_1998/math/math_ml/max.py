from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass(kw_only=True)
class Max:
    class Meta:
        name = "max"
        namespace = "http://www.w3.org/1998/Math/MathML"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
