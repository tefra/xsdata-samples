from dataclasses import dataclass, field


@dataclass
class Automatonstuff:
    class Meta:
        name = "automatonstuff"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
