from dataclasses import dataclass, field
from typing import List, Optional
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

    schema_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "@schemaLocation",
            "type": "Element",
        }
    )
    links: Optional[Links] = field(
        default=None,
        metadata={
            "name": "_links",
            "type": "Element",
        }
    )
    originator: List[Originator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    error_code: List[ErrorCode] = field(
        default_factory=list,
        metadata={
            "name": "error-code",
            "type": "Element",
        }
    )
    schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "$schema",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    fault_cause: Optional[FaultCause] = field(
        default=None,
        metadata={
            "name": "fault-cause",
            "type": "Element",
        }
    )
    characteristics: List[Characteristics] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    failures: List[Failures] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    properties: Optional[Properties] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
