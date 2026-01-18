from __future__ import annotations

from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


class LegalStatusCodeType(Enum):
    UNKNOWN = "Unknown"
    CORPORATION = "Corporation"
    JOINT_VENTURE = "JointVenture"
    PARTNERSHIP = "Partnership"
    FOREIGN_COMPANY = "ForeignCompany"
    NOT_AVAILABLE = "Not Available"
