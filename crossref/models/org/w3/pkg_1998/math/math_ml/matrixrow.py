from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Matrixrow:
    class Meta:
        name = "matrixrow"
        namespace = "http://www.w3.org/1998/Math/MathML"

    any_element: object | None = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
