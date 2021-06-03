from dataclasses import dataclass, field
from typing import Optional
from autosar.models.persistency_redundancy_handling_scope_enum import PersistencyRedundancyHandlingScopeEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PersistencyRedundancyHash:
    """
    This meta-class formally describes the usage of a Hash for the
    implementation of redundancy.

    :ivar scope: This attribute controls the scope in which the
        redundancy handling is applied.
    :ivar algorithm_family: This attribute identifies the algorithm
        family that is used to execute the CRC/Hash.
    :ivar length: This attribute describes the length of the CRC/Hash in
        the unit bits.
    :ivar initialization_vector_length: Length of the initialization
        vector.
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
        name = "PERSISTENCY-REDUNDANCY-HASH"

    scope: Optional[PersistencyRedundancyHandlingScopeEnum] = field(
        default=None,
        metadata={
            "name": "SCOPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    algorithm_family: Optional[String] = field(
        default=None,
        metadata={
            "name": "ALGORITHM-FAMILY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    initialization_vector_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "INITIALIZATION-VECTOR-LENGTH",
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
