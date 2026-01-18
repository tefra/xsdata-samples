from dataclasses import dataclass, field


@dataclass
class SchemeAgencyName:
    class Meta:
        name = "@scheme-agency-name"

    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
