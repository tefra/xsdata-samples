from __future__ import annotations

from dataclasses import dataclass

from .datatypes_base import (
    Bl,
    Ce,
    Ii,
    Ts,
)

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass(kw_only=True)
class BirthTime(Ts):
    class Meta:
        name = "birthTime"
        namespace = "urn:hl7-org:sdtc"


@dataclass(kw_only=True)
class DeceasedInd(Bl):
    class Meta:
        name = "deceasedInd"
        namespace = "urn:hl7-org:sdtc"


@dataclass(kw_only=True)
class DeceasedTime(Ts):
    class Meta:
        name = "deceasedTime"
        namespace = "urn:hl7-org:sdtc"


@dataclass(kw_only=True)
class DischargeDispositionCode(Ce):
    class Meta:
        name = "dischargeDispositionCode"
        namespace = "urn:hl7-org:sdtc"


@dataclass(kw_only=True)
class Id(Ii):
    class Meta:
        name = "id"
        namespace = "urn:hl7-org:sdtc"
