from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:shared:2009"


class WorkflowEnumType(Enum):
    """
    These are the possible values of several 'workflow' fields.

    These serve administrative purposes only. In the Frontent API you
    should only encounter 'PUBLISHED'.
    """

    FOR_PUBLICATION = "FOR PUBLICATION"
    FOR_REPUBLICATION = "FOR REPUBLICATION"
    PUBLISHED = "PUBLISHED"
    PARENT_REVOKED = "PARENT REVOKED"
    REVOKED = "REVOKED"
    FOR_DELETION = "FOR DELETION"
    DELETED = "DELETED"
    MERGED = "MERGED"
    IGNORE = "IGNORE"


WorkflowEnumType.IGNORE.__doc__ = (
    "This means that the object is ignored for workflow changes. This is "
    "mainly usefull during testing."
)
