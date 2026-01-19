from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.constraint_attachment_type import ConstraintAttachmentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataConstraintAttachmentType(ConstraintAttachmentType):
    """
    DataConstraintAttachmentType restricts the base
    ConstraintAttachmentType to only allow artefacts related to data.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
