from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .bsw_module_entry_subtypes_enum import BswModuleEntrySubtypesEnum
from .client_server_operation_subtypes_enum import (
    ClientServerOperationSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ClientServerOperationBlueprintMapping:
    """
    This class describes a specific mapping between a ClientServerOperation
    in a ClientServerInterface blueprint and a BswModuleEntry blueprint.

    :ivar blueprint_mapping_guide: This attribute offers the possibility
        to provide additional information with respect to the mapping.
    :ivar bsw_module_entry_ref: The referenced BswModuleEntry represents
        the BswModuleEntry the mapping is dedicated to.
    :ivar client_server_operation_ref: The referenced
        ClientServerOperation represents the client server operation the
        mapping is dedicated to.
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
        name = "CLIENT-SERVER-OPERATION-BLUEPRINT-MAPPING"

    blueprint_mapping_guide: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-MAPPING-GUIDE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bsw_module_entry_ref: (
        None | ClientServerOperationBlueprintMapping.BswModuleEntryRef
    ) = field(
        default=None,
        metadata={
            "name": "BSW-MODULE-ENTRY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    client_server_operation_ref: (
        None | ClientServerOperationBlueprintMapping.ClientServerOperationRef
    ) = field(
        default=None,
        metadata={
            "name": "CLIENT-SERVER-OPERATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class BswModuleEntryRef(Ref):
        dest: BswModuleEntrySubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ClientServerOperationRef(Ref):
        dest: ClientServerOperationSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
