from __future__ import annotations

from dataclasses import dataclass

from datexii.models.eu.datexii.v2.d2_logical_model_1 import D2LogicalModel1

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class D2LogicalModel(D2LogicalModel1):
    class Meta:
        name = "d2LogicalModel"
        namespace = "http://datex2.eu/schema/2/2_0"
