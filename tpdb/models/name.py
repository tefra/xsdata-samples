from dataclasses import dataclass, field


@dataclass
class Name:
    class Meta:
        name = "name"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
