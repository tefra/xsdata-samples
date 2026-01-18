from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .ar_package_subtypes_enum import ArPackageSubtypesEnum
from .boolean import Boolean
from .identifier import Identifier
from .ref import Ref
from .referrable_subtypes_enum import ReferrableSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ReferenceBase:
    """
    This meta-class establishes a basis for relative references.

    Reference bases are identified by the shortLabel which shall be unique
    in the current package.

    :ivar short_label: This is the name of the reference base. By this
        name, particular references can denote the applicable base.
    :ivar is_default: This attribute denotes if the current
        ReferenceBase is the default. Note that there can only be one
        default reference base within a package.
    :ivar is_global: This indicates that the target of the applicable
        reference can be resolved via the non-qualified shortName. This
        requires that the shortName of the target is unique within the
        package referenced in the reference base. The default is false.
        Note that the reference base also maintains a list of elements
        which may be referenced using a "global Reference".
    :ivar base_is_this_package: This indicates that this base is
        established by the current package. In this case  the
        association "package" can be derived as the qualified shortName
        of the enclosing package. If  the value of baseIsThisPackage is
        set to true then one of the following shall be true: * target of
        the association "package" shall be the enclosing package. *
        association "package" is omitted.
    :ivar global_in_package_refs: This represents the ability to express
        that global elements live in various packages which do not have
        a common ancestor package. Packages mentioned by
        ReferenceBase.globalInPackage are used in addition to the one in
        ReferenceBase.package.
    :ivar global_elements:
    :ivar package_ref: This association specifies the basis of all
        relative references with the base equals shortLabel. This
        association shall exist unless the value of baseIsThisPackage is
        set to true.
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
        name = "REFERENCE-BASE"

    short_label: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_default: Boolean | None = field(
        default=None,
        metadata={
            "name": "IS-DEFAULT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_global: Boolean | None = field(
        default=None,
        metadata={
            "name": "IS-GLOBAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    base_is_this_package: Boolean | None = field(
        default=None,
        metadata={
            "name": "BASE-IS-THIS-PACKAGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    global_in_package_refs: ReferenceBase.GlobalInPackageRefs | None = (
        field(
            default=None,
            metadata={
                "name": "GLOBAL-IN-PACKAGE-REFS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    global_elements: ReferenceBase.GlobalElements | None = field(
        default=None,
        metadata={
            "name": "GLOBAL-ELEMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    package_ref: ReferenceBase.PackageRef | None = field(
        default=None,
        metadata={
            "name": "PACKAGE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class GlobalInPackageRefs:
        global_in_package_ref: list[
            ReferenceBase.GlobalInPackageRefs.GlobalInPackageRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-IN-PACKAGE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class GlobalInPackageRef(Ref):
            dest: ArPackageSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class GlobalElements:
        """
        :ivar global_element: This attribute represents a meta-class for
            which the global referencing is supported via this reference
            base.
        """

        global_element: list[ReferrableSubtypesEnum] = field(
            default_factory=list,
            metadata={
                "name": "GLOBAL-ELEMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PackageRef(Ref):
        dest: ArPackageSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
