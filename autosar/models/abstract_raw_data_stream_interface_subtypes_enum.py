from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AbstractRawDataStreamInterfaceSubtypesEnum(Enum):
    ABSTRACT_RAW_DATA_STREAM_INTERFACE = "ABSTRACT-RAW-DATA-STREAM-INTERFACE"
    RAW_DATA_STREAM_CLIENT_INTERFACE = "RAW-DATA-STREAM-CLIENT-INTERFACE"
    RAW_DATA_STREAM_SERVER_INTERFACE = "RAW-DATA-STREAM-SERVER-INTERFACE"
