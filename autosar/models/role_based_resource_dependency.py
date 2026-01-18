from __future__ import annotations

from dataclasses import dataclass, field

from .cp_software_cluster_resource_subtypes_enum import (
    CpSoftwareClusterResourceSubtypesEnum,
)
from .identifier import Identifier
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class RoleBasedResourceDependency:
    """
    This class specifies a dependency between CpSoftwareClusterResources.

    :ivar resource_ref: Reference to resource for which the dependency
        is depicted.
    :ivar role: This is attributes characterizes the kind of dependency
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
        name = "ROLE-BASED-RESOURCE-DEPENDENCY"

    resource_ref: None | RoleBasedResourceDependency.ResourceRef = field(
        default=None,
        metadata={
            "name": "RESOURCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    role: None | Identifier = field(
        default=None,
        metadata={
            "name": "ROLE",
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
    class ResourceRef(Ref):
        dest: CpSoftwareClusterResourceSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
