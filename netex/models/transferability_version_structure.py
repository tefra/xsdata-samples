from dataclasses import dataclass, field
from typing import Optional

from .shared_usage_enumeration import SharedUsageEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferabilityVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Transferability_VersionStructure"

    can_transfer: bool | None = field(
        default=None,
        metadata={
            "name": "CanTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_named_transferees: int | None = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfNamedTransferees",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_transfer_fee: bool | None = field(
        default=None,
        metadata={
            "name": "HasTransferFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    shared_usage: SharedUsageEnumeration | None = field(
        default=None,
        metadata={
            "name": "SharedUsage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
