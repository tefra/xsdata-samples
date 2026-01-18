from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotable_type import AnnotableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class InputOutputType(AnnotableType):
    """
    InputOutputType describes the structure of an input or output to a
    process step.

    It provides a reference to the object that is the input or output.

    :ivar object_reference: ObjectReference is an abstract substitution
        head that references the object that is an input or output. It
        is substituted with a concrete reference to an explicit object
        type.
    :ivar local_id: The localID attribute is an optional identification
        for the input or output within the process.
    """

    object_reference: str | None = field(
        default=None,
        metadata={
            "name": "ObjectReference",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\)(\.[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*)?",
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
