from __future__ import annotations

from dataclasses import dataclass

from .beyond_data_horizon_error_structure import (
    BeyondDataHorizonErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class BeyondDataHorizon(BeyondDataHorizonErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
