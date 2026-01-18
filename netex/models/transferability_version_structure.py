from __future__ import annotations

from dataclasses import dataclass, field

from .shared_usage_enumeration import SharedUsageEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferabilityVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Transferability_VersionStructure"

    can_transfer: None | bool = field(
        default=None,
        metadata={
            "name": "CanTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_named_transferees: None | int = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfNamedTransferees",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_transfer_fee: None | bool = field(
        default=None,
        metadata={
            "name": "HasTransferFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    shared_usage: None | SharedUsageEnumeration = field(
        default=None,
        metadata={
            "name": "SharedUsage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
