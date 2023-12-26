from dataclasses import dataclass, field
from typing import Optional
from .shared_usage_enumeration import SharedUsageEnumeration
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransferabilityVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Transferability_VersionStructure"

    can_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_named_transferees: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfNamedTransferees",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    has_transfer_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasTransferFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    shared_usage: Optional[SharedUsageEnumeration] = field(
        default=None,
        metadata={
            "name": "SharedUsage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
