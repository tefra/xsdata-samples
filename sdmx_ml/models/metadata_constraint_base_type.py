from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.constraint_role_type import ConstraintRoleType
from sdmx_ml.models.constraint_type import ConstraintType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataConstraintBaseType(ConstraintType):
    """
    MetadataConstraintBaseType is an abstract base refinement of
    ConstraintType.

    The constraint attachment is restricted to constrainable artefacts
    related to metadata, and the only possible role is "Allowed".
    """

    role: ConstraintRoleType = field(
        init=False,
        default=ConstraintRoleType.ALLOWED,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
