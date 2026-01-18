from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean_value_variation_point import BooleanValueVariationPoint
from .category_string import CategoryString
from .diagnostic_connection_ref_conditional import (
    DiagnosticConnectionRefConditional,
)
from .diagnostic_service_table_ref_conditional import (
    DiagnosticServiceTableRefConditional,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nmtoken_string import NmtokenString
from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DiagnosticProtocol:
    """
    This meta-class represents the ability to define a diagnostic protocol.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar diagnostic_connections: This represents the collection of
        applicable DiagnosticConnections for this DiagnosticProtocol.
        This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar priority: This represents the priority of the diagnostic
        protocol in comparison to other diagnostic protocols. Lower
        numeric values represent higher protocol priority: * 0 - Highest
        protocol priority * 255 - Lowest protocol priority
    :ivar protocol_kind: This identifies the applicable protocol.
    :ivar send_resp_pend_on_trans_to_boot: The purpose of this attribute
        is to define whether or not the ECU should send a NRC 0x78
        (response pending) before transitioning to the bootloader (in
        this case the attribute shall be set to "true") or if the
        transition shall be initiated without sending NRC 0x78 (in this
        case the attribute shall be set to "false").
    :ivar service_tables: This represents the service table applicable
        for the given diagnostic protocol. This property was modified
        due to atpVariation (DirectedAssociationPattern).
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
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "DIAGNOSTIC-PROTOCOL"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: None | DiagnosticProtocol.ShortNameFragments = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: None | MultilanguageLongName = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: None | DiagnosticProtocol.Annotations = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    diagnostic_connections: None | DiagnosticProtocol.DiagnosticConnections = (
        field(
            default=None,
            metadata={
                "name": "DIAGNOSTIC-CONNECTIONS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    priority: None | PositiveIntegerValueVariationPoint = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_kind: None | NmtokenString = field(
        default=None,
        metadata={
            "name": "PROTOCOL-KIND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    send_resp_pend_on_trans_to_boot: None | BooleanValueVariationPoint = field(
        default=None,
        metadata={
            "name": "SEND-RESP-PEND-ON-TRANS-TO-BOOT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    service_tables: None | DiagnosticProtocol.ServiceTables = field(
        default=None,
        metadata={
            "name": "SERVICE-TABLES",
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
    uuid: None | str = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class DiagnosticConnections:
        diagnostic_connection_ref_conditional: list[
            DiagnosticConnectionRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-CONNECTION-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ServiceTables:
        diagnostic_service_table_ref_conditional: list[
            DiagnosticServiceTableRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-SERVICE-TABLE-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
