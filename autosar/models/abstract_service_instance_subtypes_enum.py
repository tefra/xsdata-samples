from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AbstractServiceInstanceSubtypesEnum(Enum):
    ABSTRACT_SERVICE_INSTANCE = "ABSTRACT-SERVICE-INSTANCE"
    CONSUMED_SERVICE_INSTANCE = "CONSUMED-SERVICE-INSTANCE"
    PROVIDED_SERVICE_INSTANCE = "PROVIDED-SERVICE-INSTANCE"
