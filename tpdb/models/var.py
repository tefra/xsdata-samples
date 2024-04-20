from dataclasses import dataclass, field


@dataclass
class Var:
    class Meta:
        name = "var"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
