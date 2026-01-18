from __future__ import annotations

from dataclasses import dataclass

from generali.models.org.oasis_open.docs.wsrf.bf_2.base_fault_type import (
    BaseFaultType,
)

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass
class BaseFault(BaseFaultType):
    class Meta:
        namespace = "http://docs.oasis-open.org/wsrf/bf-2"
