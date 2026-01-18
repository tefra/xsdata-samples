from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from .boolean import Boolean
from .category_string import CategoryString
from .data_filter import DataFilter
from .data_prototype_in_service_interface_ref import (
    DataPrototypeInServiceInterfaceRef,
)
from .i_signal_triggering_subtypes_enum import ISignalTriggeringSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SignalBasedFieldToISignalTriggeringMapping:
    """
    This meta-class defines the mapping of a ServiceInterface field to
    ISignalTriggerings that represent the notifier elements, the getter
    call and response, the setter call and response on a signal-based
    communication channel. .

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
    :ivar data_prototype_in_service_interface_ref: Reference to a
        DataPrototype or to an internal structure of a DataPrototype in
        the context of a ServiceInterface.
    :ivar filter: Defines an optional filter to be applied during
        translation.
    :ivar getter_call_signal_ref: Reference to the ISignalTriggering
        that is used to transport the getter method call in a signal-
        based way over a communication channel.
    :ivar getter_return_signal_ref: Reference to the ISignalTriggering
        that is used to transport the getter method response in a
        signal-based way over a communication channel.
    :ivar notifier_signal_triggering_ref: Reference to the
        ISignalTriggering that is used to transport a piece of data of a
        notifier in a signal-based way over a communication channel.
    :ivar setter_call_signal_ref: Reference to the ISignalTriggering
        that is used to transport the setter method call in a signal-
        based way over a communication channel.
    :ivar setter_return_signal_ref: Reference to the ISignalTriggering
        that is used to transport the setter method response in a
        signal-based way over a communication channel.
    :ivar transmission_trigger: Defines whether the source notifier
        element triggers the sending of the respective payload.
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
        name = "SIGNAL-BASED-FIELD-TO-I-SIGNAL-TRIGGERING-MAPPING"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: (
        None | SignalBasedFieldToISignalTriggeringMapping.ShortNameFragments
    ) = field(
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
    annotations: (
        None | SignalBasedFieldToISignalTriggeringMapping.Annotations
    ) = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_prototype_in_service_interface_ref: (
        None | DataPrototypeInServiceInterfaceRef
    ) = field(
        default=None,
        metadata={
            "name": "DATA-PROTOTYPE-IN-SERVICE-INTERFACE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    filter: None | DataFilter = field(
        default=None,
        metadata={
            "name": "FILTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    getter_call_signal_ref: (
        None | SignalBasedFieldToISignalTriggeringMapping.GetterCallSignalRef
    ) = field(
        default=None,
        metadata={
            "name": "GETTER-CALL-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    getter_return_signal_ref: (
        None | SignalBasedFieldToISignalTriggeringMapping.GetterReturnSignalRef
    ) = field(
        default=None,
        metadata={
            "name": "GETTER-RETURN-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    notifier_signal_triggering_ref: (
        None
        | SignalBasedFieldToISignalTriggeringMapping.NotifierSignalTriggeringRef
    ) = field(
        default=None,
        metadata={
            "name": "NOTIFIER-SIGNAL-TRIGGERING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    setter_call_signal_ref: (
        None | SignalBasedFieldToISignalTriggeringMapping.SetterCallSignalRef
    ) = field(
        default=None,
        metadata={
            "name": "SETTER-CALL-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    setter_return_signal_ref: (
        None | SignalBasedFieldToISignalTriggeringMapping.SetterReturnSignalRef
    ) = field(
        default=None,
        metadata={
            "name": "SETTER-RETURN-SIGNAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmission_trigger: None | Boolean = field(
        default=None,
        metadata={
            "name": "TRANSMISSION-TRIGGER",
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
    class GetterCallSignalRef(Ref):
        dest: ISignalTriggeringSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class GetterReturnSignalRef(Ref):
        dest: ISignalTriggeringSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class NotifierSignalTriggeringRef(Ref):
        dest: ISignalTriggeringSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SetterCallSignalRef(Ref):
        dest: ISignalTriggeringSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class SetterReturnSignalRef(Ref):
        dest: ISignalTriggeringSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
