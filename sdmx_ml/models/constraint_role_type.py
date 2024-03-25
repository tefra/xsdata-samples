from enum import Enum

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


class ConstraintRoleType(Enum):
    """ConstraintRoleType defines a list of roles for a content constraint.

    A constraint can state which data is present or which content is
    allowed for the constraint attachment.

    :cvar ALLOWED: The constraint contains the allowed values for
        attachable object.
    :cvar ACTUAL: The constraints contains the actual data present for
        the attachable object.
    """

    ALLOWED = "Allowed"
    ACTUAL = "Actual"
