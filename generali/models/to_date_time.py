from dataclasses import dataclass, field


@dataclass
class ToDateTime:
    class Meta:
        name = "to-date-time"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    format: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
