from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.constraint_attachment_type import ConstraintAttachmentType
from sdmx_ml.models.constraint_base_type import ConstraintBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class ConstraintType(ConstraintBaseType):
    """
    ConstraintType is an abstract base type that specific types of
    constraints (data and metadata) restrict and extend to describe their
    details.

    :ivar constraint_attachment: ConstraintAttachment describes the
        collection of constrainable artefacts that the constraint is
        attached to.
    """

    constraint_attachment: None | ConstraintAttachmentType = field(
        default=None,
        metadata={
            "name": "ConstraintAttachment",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
        },
    )
