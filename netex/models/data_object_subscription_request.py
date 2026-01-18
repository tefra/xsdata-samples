from __future__ import annotations

from dataclasses import dataclass

from .data_object_subscription_structure import DataObjectSubscriptionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectSubscriptionRequest(DataObjectSubscriptionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
