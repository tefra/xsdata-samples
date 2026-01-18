from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.error_element_type_level import (
    ErrorElementTypeLevel,
)
from generali.models.com.generali.xmlns.services.program.feedback_program_service.v1.error_element_type_type import (
    ErrorElementTypeType,
)

__NAMESPACE__ = (
    "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"
)


@dataclass(kw_only=True)
class ErrorElementType:
    code: str = field(
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        }
    )
    type_value: ErrorElementTypeType = field(
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        }
    )
    level: ErrorElementTypeLevel = field(
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://xmlns.generali.com/services/program/FeedbackProgramService/v1",
            "required": True,
        }
    )
