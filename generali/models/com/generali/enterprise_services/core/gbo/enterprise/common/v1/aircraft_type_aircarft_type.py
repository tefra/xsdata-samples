from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


class AircraftTypeAircarftType(StrEnum):
    FIXED_WING_AIRCRAFT = "Fixed Wing Aircraft"
    ROTOR_WING_AIRCRAFT = "Rotor Wing Aircraft"
