from __future__ import annotations

from dataclasses import dataclass, field

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

    schema_location: None | str = field(
        default=None,
        metadata={
            "name": "@schemaLocation",
            "type": "Element",
        },
    )
    links: None | Links = field(
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
    schema: None | str = field(
        default=None,
        metadata={
            "name": "$schema",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    fault_cause: None | FaultCause = field(
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
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
        },
    )
    properties: None | Properties = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
