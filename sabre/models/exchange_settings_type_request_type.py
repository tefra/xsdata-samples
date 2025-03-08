from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class ExchangeSettingsTypeRequestType(Enum):
    BASIC = "basic"
    CONTEXT = "context"
