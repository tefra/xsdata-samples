from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.text_type import TextType
from sdmx_ml.models.transition_base_type import TransitionBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TransitionType(TransitionBaseType):
    """
    TransitionType describes the details of a transition, which is an
    expression in a textual or formalised way of the transformation of data
    between two specific operations performed on the data.

    :ivar target_step: TargetStep references a process step within the
        process that should be transitioned to, should the conditions
        described be met.
    :ivar condition: Condition is a textual description of the
        conditions to be met in order for the target step to be
        proceeded to. It is informational only (not machine-actionable),
        and may be supplied in multiple, parallel-language form.
    :ivar local_id: The localID attribute is an optional identification
        for the transition within the process.
    """

    target_step: str | None = field(
        default=None,
        metadata={
            "name": "TargetStep",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*",
        },
    )
    condition: tuple[TextType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
    local_id: str | None = field(
        default=None,
        metadata={
            "name": "localID",
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
