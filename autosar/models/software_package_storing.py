from __future__ import annotations

from dataclasses import dataclass, field

from .ref import Ref
from .software_package_storing_enum import SoftwarePackageStoringEnum
from .software_package_subtypes_enum import SoftwarePackageSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoftwarePackageStoring:
    """
    This meta-class provides the ability to specify whether and where the
    referenced SoftwarePackage is stored.

    :ivar storing: This attribute clarifies whether and where the
        referenced SoftwarePackage is stored.
    :ivar transfer_refs: This reference identifies the
        SoftwarePackage(s) to be transferred in the enclosing
        SoftwarePackageStep.
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
        name = "SOFTWARE-PACKAGE-STORING"

    storing: None | SoftwarePackageStoringEnum = field(
        default=None,
        metadata={
            "name": "STORING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transfer_refs: None | SoftwarePackageStoring.TransferRefs = field(
        default=None,
        metadata={
            "name": "TRANSFER-REFS",
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

    @dataclass
    class TransferRefs:
        transfer_ref: list[SoftwarePackageStoring.TransferRefs.TransferRef] = (
            field(
                default_factory=list,
                metadata={
                    "name": "TRANSFER-REF",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

        @dataclass
        class TransferRef(Ref):
            dest: None | SoftwarePackageSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
