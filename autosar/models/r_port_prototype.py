from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.category_string import CategoryString
from autosar.models.client_com_spec import ClientComSpec
from autosar.models.client_server_annotation import ClientServerAnnotation
from autosar.models.crypto_r_port_com_spec import CryptoRPortComSpec
from autosar.models.delegated_port_annotation import DelegatedPortAnnotation
from autosar.models.identifier import Identifier
from autosar.models.io_hw_abstraction_server_annotation import IoHwAbstractionServerAnnotation
from autosar.models.mode_port_annotation import ModePortAnnotation
from autosar.models.mode_switch_receiver_com_spec import ModeSwitchReceiverComSpec
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.nonqueued_receiver_com_spec import NonqueuedReceiverComSpec
from autosar.models.nv_data_port_annotation import NvDataPortAnnotation
from autosar.models.nv_require_com_spec import NvRequireComSpec
from autosar.models.parameter_port_annotation import ParameterPortAnnotation
from autosar.models.parameter_require_com_spec import ParameterRequireComSpec
from autosar.models.persistency_data_required_com_spec import PersistencyDataRequiredComSpec
from autosar.models.port_interface_subtypes_enum import PortInterfaceSubtypesEnum
from autosar.models.queued_receiver_com_spec import QueuedReceiverComSpec
from autosar.models.r_port_prototype_props import RPortPrototypeProps
from autosar.models.receiver_annotation import ReceiverAnnotation
from autosar.models.ref import Ref
from autosar.models.sender_annotation import SenderAnnotation
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.trigger_port_annotation import TriggerPortAnnotation

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RPortPrototype:
    """
    Component port requiring a certain port interface.

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
    :ivar client_server_annotations: Annotation of this PortPrototype
        with respect to client/server communication.
    :ivar delegated_port_annotation: Annotations on this delegated port.
    :ivar io_hw_abstraction_server_annotations: Annotations on this IO
        Hardware Abstraction port.
    :ivar mode_port_annotations: Annotations on this mode port.
    :ivar nv_data_port_annotations: Annotations on this non voilatile
        data port.
    :ivar parameter_port_annotations: Annotations on this parameter
        port.
    :ivar port_prototype_props: This attribute allows for the definition
        of further qualification of the semantics of a PortPrototype.
    :ivar sender_receiver_annotations: Collection of annotations of this
        ports sender/receiver communication.
    :ivar trigger_port_annotations: Annotations on this trigger port.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar required_com_specs: Required communication attributes, one for
        each interface element.
    :ivar required_interface_tref: The interface that this port
        requires.
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
        name = "R-PORT-PROTOTYPE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["RPortPrototype.ShortNameFragments"] = field(
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
    annotations: Optional["RPortPrototype.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    client_server_annotations: Optional["RPortPrototype.ClientServerAnnotations"] = field(
        default=None,
        metadata={
            "name": "CLIENT-SERVER-ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    delegated_port_annotation: Optional[DelegatedPortAnnotation] = field(
        default=None,
        metadata={
            "name": "DELEGATED-PORT-ANNOTATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    io_hw_abstraction_server_annotations: Optional["RPortPrototype.IoHwAbstractionServerAnnotations"] = field(
        default=None,
        metadata={
            "name": "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mode_port_annotations: Optional["RPortPrototype.ModePortAnnotations"] = field(
        default=None,
        metadata={
            "name": "MODE-PORT-ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nv_data_port_annotations: Optional["RPortPrototype.NvDataPortAnnotations"] = field(
        default=None,
        metadata={
            "name": "NV-DATA-PORT-ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    parameter_port_annotations: Optional["RPortPrototype.ParameterPortAnnotations"] = field(
        default=None,
        metadata={
            "name": "PARAMETER-PORT-ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    port_prototype_props: Optional[RPortPrototypeProps] = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    sender_receiver_annotations: Optional["RPortPrototype.SenderReceiverAnnotations"] = field(
        default=None,
        metadata={
            "name": "SENDER-RECEIVER-ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    trigger_port_annotations: Optional["RPortPrototype.TriggerPortAnnotations"] = field(
        default=None,
        metadata={
            "name": "TRIGGER-PORT-ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    required_com_specs: Optional["RPortPrototype.RequiredComSpecs"] = field(
        default=None,
        metadata={
            "name": "REQUIRED-COM-SPECS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    required_interface_tref: Optional["RPortPrototype.RequiredInterfaceTref"] = field(
        default=None,
        metadata={
            "name": "REQUIRED-INTERFACE-TREF",
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
    class ClientServerAnnotations:
        client_server_annotation: List[ClientServerAnnotation] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-SERVER-ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class IoHwAbstractionServerAnnotations:
        io_hw_abstraction_server_annotation: List[IoHwAbstractionServerAnnotation] = field(
            default_factory=list,
            metadata={
                "name": "IO-HW-ABSTRACTION-SERVER-ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ModePortAnnotations:
        mode_port_annotation: List[ModePortAnnotation] = field(
            default_factory=list,
            metadata={
                "name": "MODE-PORT-ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class NvDataPortAnnotations:
        nv_data_port_annotation: List[NvDataPortAnnotation] = field(
            default_factory=list,
            metadata={
                "name": "NV-DATA-PORT-ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ParameterPortAnnotations:
        parameter_port_annotation: List[ParameterPortAnnotation] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-PORT-ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class SenderReceiverAnnotations:
        receiver_annotation: List[ReceiverAnnotation] = field(
            default_factory=list,
            metadata={
                "name": "RECEIVER-ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        sender_annotation: List[SenderAnnotation] = field(
            default_factory=list,
            metadata={
                "name": "SENDER-ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class TriggerPortAnnotations:
        trigger_port_annotation: List[TriggerPortAnnotation] = field(
            default_factory=list,
            metadata={
                "name": "TRIGGER-PORT-ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class RequiredComSpecs:
        client_com_spec: List[ClientComSpec] = field(
            default_factory=list,
            metadata={
                "name": "CLIENT-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        crypto_r_port_com_spec: List[CryptoRPortComSpec] = field(
            default_factory=list,
            metadata={
                "name": "CRYPTO-R-PORT-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        mode_switch_receiver_com_spec: List[ModeSwitchReceiverComSpec] = field(
            default_factory=list,
            metadata={
                "name": "MODE-SWITCH-RECEIVER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        nonqueued_receiver_com_spec: List[NonqueuedReceiverComSpec] = field(
            default_factory=list,
            metadata={
                "name": "NONQUEUED-RECEIVER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        nv_require_com_spec: List[NvRequireComSpec] = field(
            default_factory=list,
            metadata={
                "name": "NV-REQUIRE-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        parameter_require_com_spec: List[ParameterRequireComSpec] = field(
            default_factory=list,
            metadata={
                "name": "PARAMETER-REQUIRE-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        persistency_data_required_com_spec: List[PersistencyDataRequiredComSpec] = field(
            default_factory=list,
            metadata={
                "name": "PERSISTENCY-DATA-REQUIRED-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        queued_receiver_com_spec: List[QueuedReceiverComSpec] = field(
            default_factory=list,
            metadata={
                "name": "QUEUED-RECEIVER-COM-SPEC",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class RequiredInterfaceTref(Ref):
        dest: Optional[PortInterfaceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )