from __future__ import annotations

from dataclasses import dataclass, field

from .constant_specification_subtypes_enum import (
    ConstantSpecificationSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ConstantSpecificationMapping:
    """
    This meta-class is used to create an association of two
    ConstantSpecifications.

    One ConstantSpecification is supposed to be defined in the application
    domain while the other should be defined in the implementation domain.
    Hence the ConstantSpecificationMapping needs to be used where a
    ConstantSpecification defined in one domain needs to be associated to a
    ConstantSpecification in the other domain. This information is crucial
    for the RTE generator.

    :ivar appl_constant_ref: A ConstantSpecification defined in the
        application domain.
    :ivar impl_constant_ref: A ConstantSpecification defined in the
        implementation domain.
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
        name = "CONSTANT-SPECIFICATION-MAPPING"

    appl_constant_ref: None | ConstantSpecificationMapping.ApplConstantRef = (
        field(
            default=None,
            metadata={
                "name": "APPL-CONSTANT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    impl_constant_ref: None | ConstantSpecificationMapping.ImplConstantRef = (
        field(
            default=None,
            metadata={
                "name": "IMPL-CONSTANT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass(kw_only=True)
    class ApplConstantRef(Ref):
        dest: ConstantSpecificationSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ImplConstantRef(Ref):
        dest: ConstantSpecificationSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
