from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.computation_type import ComputationType
from sdmx_ml.models.input_output_type import InputOutputType
from sdmx_ml.models.process_step_base_type import ProcessStepBaseType
from sdmx_ml.models.transition_type import TransitionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ProcessStepType(ProcessStepBaseType):
    """
    ProcessStepType describes the structure of a process step.

    A nested process step is automatically sub-ordinate, and followed as
    the next step. If the following step is conditional, it should be
    referenced in a transition.

    :ivar input: Input references an object which is an input to the
        process step.
    :ivar output: Output references an object which is an output form
        the process step.
    :ivar computation: Computation describes the computations involved
        in the process, in any form desired by the user (these are
        informational rather than machine-actionable), and so may be
        supplied in multiple, parallel-language versions.
    :ivar transition: Transition describes the next process steps. Each
        transition in a process step should be evaluated, allowing for
        multiple process step branches from a single process step.
    :ivar process_step: ProcessStep defines a process step, which is a
        specific operation, performed on data in order to validate or to
        derive new information according to a given set of rules.
    """

    input: tuple[InputOutputType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Input",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    output: tuple[InputOutputType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Output",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    computation: ComputationType | None = field(
        default=None,
        metadata={
            "name": "Computation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    transition: tuple[TransitionType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    process_step: tuple[ProcessStepType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ProcessStep",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
