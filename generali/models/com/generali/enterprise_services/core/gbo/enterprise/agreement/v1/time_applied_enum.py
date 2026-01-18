from __future__ import annotations

from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class TimeAppliedEnum(Enum):
    ON_RENEWAL = "OnRenewal"
    ON_EXPIRY = "OnExpiry"
    FIRST_INSTALMENT = "FirstInstalment"
    LAST_INSTALMENT = "LastInstalment"
    SKIP_FIRST_INSTALMENT = "SkipFirstInstalment"
    EQUALLY_ACROSS_ALL_INSTALMENT = "EquallyAcrossAllInstalment"
