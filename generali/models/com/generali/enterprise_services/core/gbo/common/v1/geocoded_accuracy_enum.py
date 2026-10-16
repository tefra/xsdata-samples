from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class GeocodedAccuracyEnum(StrEnum):
    POSTCODE = "Postcode"
    STREET = "Street"
