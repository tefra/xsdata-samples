from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .boolean import Boolean
from .bsw_module_entry_subtypes_enum import BswModuleEntrySubtypesEnum
from .identifier import Identifier
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BswModuleClientServerEntry:
    """
    This meta-class represents a single API entry into the BSW module or
    cluster that has the ability to be called in client-server fashion via
    the BSW Scheduler.

    In this regard it is more special than BswModuleEntry and can be seen
    as a wrapper around the BswModuleEntry to which it refers (property
    encapsulatedEntry).

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar encapsulated_entry_ref: The underlying BswModuleEntry.
    :ivar is_reentrant: Reentrancy from the viewpoint of clients
        invoking the service via the BSW Scheduler: * True: Enables the
        service to be invoked again, before the service has finished. *
        False: It is prohibited to invoke the service again before is
        has finished.
    :ivar is_synchronous: Synchronicity from the viewpoint of clients
        invoking the service via the BSW Scheduler: * True: This calls a
        synchronous service, i.e. the service is completed when the call
        returns. * False: The service (on semantical level) may not be
        complete when the call returns.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "BSW-MODULE-CLIENT-SERVER-ENTRY"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: BswModuleClientServerEntry.ShortNameFragments | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    encapsulated_entry_ref: BswModuleClientServerEntry.EncapsulatedEntryRef | None = field(
        default=None,
        metadata={
            "name": "ENCAPSULATED-ENTRY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_reentrant: Boolean | None = field(
        default=None,
        metadata={
            "name": "IS-REENTRANT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    is_synchronous: Boolean | None = field(
        default=None,
        metadata={
            "name": "IS-SYNCHRONOUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EncapsulatedEntryRef(Ref):
        dest: BswModuleEntrySubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
