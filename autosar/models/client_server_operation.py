from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .ap_application_error_set_subtypes_enum import (
    ApApplicationErrorSetSubtypesEnum,
)
from .ap_application_error_subtypes_enum import ApApplicationErrorSubtypesEnum
from .application_error_subtypes_enum import ApplicationErrorSubtypesEnum
from .argument_data_prototype import ArgumentDataPrototype
from .boolean import Boolean
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ClientServerOperation:
    """
    @RESTRICT_TO_STANDARD:CP:AP!

    An operation declared within the scope of a client/server interface.
    @RESTRICT_TO_STANDARD:FO! A remote procedure call declared within the
    scope of the current interface. @END_RESTRICT_TO_STANDARD!

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
    :ivar arguments: An argument of this ClientServerOperation The upper
        multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar diag_arg_integrity: This attribute shall only be used in the
        implementation of diagnostic routines to support the case where
        input and output arguments are allocated in a shared buffer and
        might unintentionally overwrite input arguments by tentative
        write operations to output arguments. This situation can happen
        during sliced execution or while output parameters are arrays
        (call by reference). The value true means that the
        ClientServerOperation is aware of the usage of a shared buffer
        and takes precautions to avoid unintentional overwrite of input
        arguments. If the attribute does not exist or is set to false
        the ClientServerOperation does not have to consider the usage of
        a shared buffer.
    :ivar fire_and_forget: This attribute defines whether this method is
        a fire&amp;forget method (true) or not (false).
    :ivar possible_ap_error_refs: This reference identifies
        AdaptivePlatformApplicationErrors as a possible error raised by
        the enclosing ClientServerOperation.
    :ivar possible_ap_error_set_refs: This reference represents the
        ability to refer to an entire group of ApApplicationErrors as
        one model element instead of having to refer to all the
        represented ApApplicationErrors separately.
    :ivar possible_error_refs: Possible errors that may by raised by the
        referring operation.
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
        name = "CLIENT-SERVER-OPERATION"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: ClientServerOperation.ShortNameFragments | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: AdminData | None = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: ClientServerOperation.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    arguments: ClientServerOperation.Arguments | None = field(
        default=None,
        metadata={
            "name": "ARGUMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    diag_arg_integrity: Boolean | None = field(
        default=None,
        metadata={
            "name": "DIAG-ARG-INTEGRITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    fire_and_forget: Boolean | None = field(
        default=None,
        metadata={
            "name": "FIRE-AND-FORGET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    possible_ap_error_refs: ClientServerOperation.PossibleApErrorRefs | None = field(
        default=None,
        metadata={
            "name": "POSSIBLE-AP-ERROR-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    possible_ap_error_set_refs: ClientServerOperation.PossibleApErrorSetRefs | None = field(
        default=None,
        metadata={
            "name": "POSSIBLE-AP-ERROR-SET-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    possible_error_refs: ClientServerOperation.PossibleErrorRefs | None = field(
        default=None,
        metadata={
            "name": "POSSIBLE-ERROR-REFS",
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
    uuid: str | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
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
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Arguments:
        argument_data_prototype: list[ArgumentDataPrototype] = field(
            default_factory=list,
            metadata={
                "name": "ARGUMENT-DATA-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PossibleApErrorRefs:
        possible_ap_error_ref: list[
            ClientServerOperation.PossibleApErrorRefs.PossibleApErrorRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "POSSIBLE-AP-ERROR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PossibleApErrorRef(Ref):
            dest: ApApplicationErrorSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class PossibleApErrorSetRefs:
        possible_ap_error_set_ref: list[
            ClientServerOperation.PossibleApErrorSetRefs.PossibleApErrorSetRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "POSSIBLE-AP-ERROR-SET-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PossibleApErrorSetRef(Ref):
            dest: ApApplicationErrorSetSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class PossibleErrorRefs:
        possible_error_ref: list[
            ClientServerOperation.PossibleErrorRefs.PossibleErrorRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "POSSIBLE-ERROR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class PossibleErrorRef(Ref):
            dest: ApplicationErrorSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
