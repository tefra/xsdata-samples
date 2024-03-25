from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.nameable_type import NameableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ProcessStepBaseType(NameableType):
    """
    ProcessStepBaseType is an abstract base type used as the basis for the
    ProcessStepType.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
