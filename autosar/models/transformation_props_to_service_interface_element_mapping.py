from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.category_string import CategoryString
from autosar.models.client_server_operation_subtypes_enum import ClientServerOperationSubtypesEnum
from autosar.models.field_subtypes_enum import FieldSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.tlv_data_id_definition_set_subtypes_enum import TlvDataIdDefinitionSetSubtypesEnum
from autosar.models.transformation_props_subtypes_enum import TransformationPropsSubtypesEnum
from autosar.models.variable_data_prototype_subtypes_enum import VariableDataPrototypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TransformationPropsToServiceInterfaceElementMapping:
    """This meta-class represents the ability to associate a ServiceInterface
    element with TransformationProps.

    The referenced elements of the Service Interface will be serialized
    according to the settings defined in the TransformationProps.

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
        object in question.  More elaborate documentation, (in
        particular how the object is built or used) should go to
        "introduction".
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
    :ivar event_refs: This represents the reference to one or several
        events of one ServiceInterface.
    :ivar field_refs: This represents the reference to one or several
        fields of one ServiceInterface.
    :ivar method_refs: This represents the reference to one or several
        methods of one ServiceInterface.
    :ivar tlv_data_id_definition_refs: This reference identifies the
        TlvDataIdDefinitions relevant for the enclosing
        TransformationPropsToServiceInterfaceMapping.
    :ivar transformation_props_ref: This represents the reference to the
        applicable Serialization properties.
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
        different AUTOSAR models.  The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed.  An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "TRANSFORMATION-PROPS-TO-SERVICE-INTERFACE-ELEMENT-MAPPING"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["TransformationPropsToServiceInterfaceElementMapping.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["TransformationPropsToServiceInterfaceElementMapping.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    event_refs: Optional["TransformationPropsToServiceInterfaceElementMapping.EventRefs"] = field(
        default=None,
        metadata={
            "name": "EVENT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    field_refs: Optional["TransformationPropsToServiceInterfaceElementMapping.FieldRefs"] = field(
        default=None,
        metadata={
            "name": "FIELD-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    method_refs: Optional["TransformationPropsToServiceInterfaceElementMapping.MethodRefs"] = field(
        default=None,
        metadata={
            "name": "METHOD-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tlv_data_id_definition_refs: Optional["TransformationPropsToServiceInterfaceElementMapping.TlvDataIdDefinitionRefs"] = field(
        default=None,
        metadata={
            "name": "TLV-DATA-ID-DEFINITION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    transformation_props_ref: Optional["TransformationPropsToServiceInterfaceElementMapping.TransformationPropsRef"] = field(
        default=None,
        metadata={
            "name": "TRANSFORMATION-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class EventRefs:
        event_ref: List["TransformationPropsToServiceInterfaceElementMapping.EventRefs.EventRef"] = field(
            default_factory=list,
            metadata={
                "name": "EVENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class EventRef(Ref):
            dest: Optional[VariableDataPrototypeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class FieldRefs:
        field_ref: List["TransformationPropsToServiceInterfaceElementMapping.FieldRefs.FieldRef"] = field(
            default_factory=list,
            metadata={
                "name": "FIELD-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class FieldRef(Ref):
            dest: Optional[FieldSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class MethodRefs:
        method_ref: List["TransformationPropsToServiceInterfaceElementMapping.MethodRefs.MethodRef"] = field(
            default_factory=list,
            metadata={
                "name": "METHOD-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class MethodRef(Ref):
            dest: Optional[ClientServerOperationSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class TlvDataIdDefinitionRefs:
        tlv_data_id_definition_ref: List["TransformationPropsToServiceInterfaceElementMapping.TlvDataIdDefinitionRefs.TlvDataIdDefinitionRef"] = field(
            default_factory=list,
            metadata={
                "name": "TLV-DATA-ID-DEFINITION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class TlvDataIdDefinitionRef(Ref):
            dest: Optional[TlvDataIdDefinitionSetSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class TransformationPropsRef(Ref):
        dest: Optional[TransformationPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
