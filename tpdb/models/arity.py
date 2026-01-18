from dataclasses import dataclass, field


@dataclass
class Arity:
    class Meta:
        name = "arity"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
