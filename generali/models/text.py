from dataclasses import dataclass, field


@dataclass
class Text:
    class Meta:
        name = "text"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    description: object | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
