from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .communication_direction_type import CommunicationDirectionType
from .i_signal_i_pdu_group_subtypes_enum import ISignalIPduGroupSubtypesEnum
from .i_signal_i_pdu_ref_conditional import ISignalIPduRefConditional
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .nm_pdu_ref_conditional import NmPduRefConditional
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ISignalIPduGroup:
    """The AUTOSAR COM Layer is able to start and to stop sending and receiving
    configurable groups of I-Pdus during runtime.

    An ISignalIPduGroup contains either ISignalIPdus or
    ISignalIPduGroups.

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
    :ivar communication_direction: This attribute determines in which
        direction IPdus that are contained in this IPduGroup will be
        transmitted (communication direction can be either In or Out).
    :ivar communication_mode: This attribute defines the use-case for
        this ISignalIPduGroup (e.g. diagnostic, debugging etc.). For
        example, in a diagnostic mode all IPdus - which are not involved
        in diagnostic - are disabled. The use cases are not limited to a
        fixed enumeration and can be specified as a string.
    :ivar contained_i_signal_i_pdu_group_refs: An I-Pdu group can be
        included in other I-Pdu groups. Contained I-Pdu groups shall not
        be referenced by the EcuInstance.
    :ivar i_signal_i_pdus: This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar nm_pdus: This property was modified due to atpVariation
        (DirectedAssociationPattern).
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
        name = "I-SIGNAL-I-PDU-GROUP"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["ISignalIPduGroup.ShortNameFragments"] = field(
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
    annotations: Optional["ISignalIPduGroup.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    communication_direction: Optional[CommunicationDirectionType] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-DIRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    communication_mode: Optional[String] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    contained_i_signal_i_pdu_group_refs: Optional["ISignalIPduGroup.ContainedISignalIPduGroupRefs"] = field(
        default=None,
        metadata={
            "name": "CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    i_signal_i_pdus: Optional["ISignalIPduGroup.ISignalIPdus"] = field(
        default=None,
        metadata={
            "name": "I-SIGNAL-I-PDUS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_pdus: Optional["ISignalIPduGroup.NmPdus"] = field(
        default=None,
        metadata={
            "name": "NM-PDUS",
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
    class ContainedISignalIPduGroupRefs:
        contained_i_signal_i_pdu_group_ref: List["ISignalIPduGroup.ContainedISignalIPduGroupRefs.ContainedISignalIPduGroupRef"] = field(
            default_factory=list,
            metadata={
                "name": "CONTAINED-I-SIGNAL-I-PDU-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ContainedISignalIPduGroupRef(Ref):
            dest: Optional[ISignalIPduGroupSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class ISignalIPdus:
        i_signal_i_pdu_ref_conditional: List[ISignalIPduRefConditional] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-I-PDU-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class NmPdus:
        nm_pdu_ref_conditional: List[NmPduRefConditional] = field(
            default_factory=list,
            metadata={
                "name": "NM-PDU-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
