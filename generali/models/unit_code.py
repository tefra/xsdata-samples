from dataclasses import dataclass, field


@dataclass
class UnitCode:
    class Meta:
        name = "@unit-code"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
