from dataclasses import dataclass, field


@dataclass
class SchemeName:
    class Meta:
        name = "@scheme-name"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
