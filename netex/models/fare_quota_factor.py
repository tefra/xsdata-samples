from __future__ import annotations

from dataclasses import dataclass

from .fare_quota_factor_version_structure import (
    FareQuotaFactorVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareQuotaFactor(FareQuotaFactorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
