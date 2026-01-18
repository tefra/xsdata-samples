from dataclasses import dataclass, field
from typing import Optional

from generali.models.amount import (
    Characteristics,
    ErrorCode,
    Failures,
    FaultCause,
    Originator,
    Properties,
)
from generali.models.links import Links


@dataclass
class Models:
    class Meta:
        name = "models"

    schema_location: str | None = field(
        default=None,
        metadata={
            "name": "@schemaLocation",
            "type": "Element",
        },
    )
    links: Links | None = field(
        default=None,
        metadata={
            "name": "_links",
            "type": "Element",
        },
    )
    originator: list[Originator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    error_code: list[ErrorCode] = field(
        default_factory=list,
        metadata={
            "name": "error-code",
            "type": "Element",
        },
    )
    schema: str | None = field(
        default=None,
        metadata={
            "name": "$schema",
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    description: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    fault_cause: FaultCause | None = field(
        default=None,
        metadata={
            "name": "fault-cause",
            "type": "Element",
        },
    )
    characteristics: list[Characteristics] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    failures: list[Failures] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    type_value: str | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: Properties | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
