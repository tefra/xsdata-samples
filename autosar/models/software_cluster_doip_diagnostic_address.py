from dataclasses import dataclass, field
from typing import Optional
from .positive_integer import PositiveInteger
from .software_cluster_diagnostic_address_semantics_enum import SoftwareClusterDiagnosticAddressSemanticsEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoftwareClusterDoipDiagnosticAddress:
    """
    This meta-class represents the ability to define a diagnostic address
    specifically for the DoIP case.

    :ivar address_semantics: This attribute clarifies whether the
        address value shall be interpreted as a physical or a functional
        address.
    :ivar diagnostic_address: This attribute represents the collection
        of diagnostic addresses the SoftwareCluster occupies.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "SOFTWARE-CLUSTER-DOIP-DIAGNOSTIC-ADDRESS"

    address_semantics: Optional[SoftwareClusterDiagnosticAddressSemanticsEnum] = field(
        default=None,
        metadata={
            "name": "ADDRESS-SEMANTICS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    diagnostic_address: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "DIAGNOSTIC-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
