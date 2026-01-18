from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PersistencyDeploymentSubtypesEnum(Enum):
    PERSISTENCY_DEPLOYMENT = "PERSISTENCY-DEPLOYMENT"
    PERSISTENCY_FILE_STORAGE = "PERSISTENCY-FILE-STORAGE"
    PERSISTENCY_KEY_VALUE_STORAGE = "PERSISTENCY-KEY-VALUE-STORAGE"
