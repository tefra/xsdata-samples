from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class TypeStatus2(StrEnum):
    """
    The status of the service fees.

    Properties
    ----------
    ISSUED
        The service fee has been issued.
    READY_TO_ISSUE
        The service fee is ready to be issued.
    ISSUE_LATER
        The service fee can be issued later.
    """

    ISSUED = "Issued"
    READY_TO_ISSUE = "ReadyToIssue"
    ISSUE_LATER = "IssueLater"
