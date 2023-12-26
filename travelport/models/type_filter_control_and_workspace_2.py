from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeFilterControlAndWorkspace2(Enum):
    """
    Allow the filtering of Workspace and Control or specify no filtering at all.
    """

    WORKSPACE_ONLY = "WorkspaceOnly"
    CONTROL_ONLY = "ControlOnly"
    ALL = "All"
