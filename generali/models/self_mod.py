from dataclasses import dataclass, field


@dataclass
class Self:
    class Meta:
        name = "self"

    href: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
