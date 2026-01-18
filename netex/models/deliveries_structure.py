from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .data_object_delivery import DataObjectDelivery

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeliveriesStructure:
    data_object_delivery: Iterable[DataObjectDelivery] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectDelivery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
