from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PersistencyDeploymentElementSubtypesEnum(StrEnum):
    PERSISTENCY_DEPLOYMENT_ELEMENT = "PERSISTENCY-DEPLOYMENT-ELEMENT"
    PERSISTENCY_FILE = "PERSISTENCY-FILE"
    PERSISTENCY_KEY_VALUE_PAIR = "PERSISTENCY-KEY-VALUE-PAIR"
