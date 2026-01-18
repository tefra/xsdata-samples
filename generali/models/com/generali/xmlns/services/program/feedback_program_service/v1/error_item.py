from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass
class ErrorItem:
    class Meta:
        namespace = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"

    code: str | None = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "required": True,
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "required": True,
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "required": True,
        },
    )
    level: str | None = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Element",
            "required": True,
        },
    )
