from __future__ import annotations

from dataclasses import dataclass, field

from .ref import Ref
from .someip_collection_props import SomeipCollectionProps
from .someip_method_deployment_subtypes_enum import (
    SomeipMethodDeploymentSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SomeipMethodProps:
    """
    This meta-class allows to set configuration options for a method in the
    service instance.

    :ivar collection_props: Collection of timing attributes configurable
        for a method that is provided or requested by a Service
        Instance.
    :ivar method_ref: Reference to the method for which the
        SomeipMethodProps are applicable.
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
        name = "SOMEIP-METHOD-PROPS"

    collection_props: None | SomeipCollectionProps = field(
        default=None,
        metadata={
            "name": "COLLECTION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    method_ref: None | SomeipMethodProps.MethodRef = field(
        default=None,
        metadata={
            "name": "METHOD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
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
    class MethodRef(Ref):
        dest: SomeipMethodDeploymentSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
