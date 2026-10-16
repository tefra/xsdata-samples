from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class UnderwriterRoleTypeUnderwriterType(StrEnum):
    ASSISTANT_UNDERWRITER = "Assistant Underwriter"
    UNDERWRITER = "Underwriter"
    BACKUP_UNDERWRITER = "Backup Underwriter"
    CHIEF_UNDERWRITER = "Chief Underwriter"
