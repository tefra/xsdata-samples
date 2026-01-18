from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.constraint_attachment_type import ConstraintAttachmentType
from sdmx_ml.models.constraint_base_type import ConstraintBaseType
from sdmx_ml.models.constraint_role_type import ConstraintRoleType
from sdmx_ml.models.release_calendar_type import ReleaseCalendarType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class ConstraintType(ConstraintBaseType):
    """
    ConstraintType is an abstract base type that specific types of
    constraints (data and metadata) restrict and extend to describe their
    details.

    These constraint types both define a constraint attachment and a
    release calendar.

    :ivar constraint_attachment: ConstraintAttachment describes the
        collection of constrainable artefacts that the constraint is
        attached to.
    :ivar release_calendar: ReleaseCalendar defines dates on which the
        constrained data is to be made available.
    :ivar role: The role attribute indicates whether this constraint
        states what data is actually present for the constraint
        attachment, or if it defines what content is allowed.
    """

    constraint_attachment: None | ConstraintAttachmentType = field(
        default=None,
        metadata={
            "name": "ConstraintAttachment",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    release_calendar: None | ReleaseCalendarType = field(
        default=None,
        metadata={
            "name": "ReleaseCalendar",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    role: ConstraintRoleType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
