from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .contained_i_pdu_props import ContainedIPduProps
from .i_pdu_timing import IPduTiming
from .i_signal_to_i_pdu_mapping import ISignalToIPduMapping
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment
from .signal_i_pdu_counter import SignalIPduCounter
from .signal_i_pdu_replication import SignalIPduReplication

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ISignalIPdu:
    """
    Represents the IPdus handled by Com.

    The ISignalIPdu assembled and disassembled in AUTOSAR COM consists of
    one or more signals. In case no multiplexing is performed this IPdu is
    routed to/from the Interface Layer. A maximum of one dynamic length
    signal per IPdu is allowed.

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
    :ivar has_dynamic_length: This attribute defines whether the Pdu has
        dynamic length (true) or not (false). Please note that the usage
        of this attribute is restricted by [constr_3448].
    :ivar length: Pdu length in bytes. In case of dynamic length IPdus
        (containing a dynamical length signal), this value indicates the
        maximum data length. It should be noted that in former AUTOSAR
        releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this
        parameter was defined in bits. The Pdu length of zero bytes is
        allowed.
    :ivar meta_data_length: Number of additional bytes of MetaData in
        the PDU data field. The MetaData contains auxiliary information
        for the PDU, e.g. the CAN ID.
    :ivar contained_i_pdu_props: Defines whether this IPdu may be
        collected inside a ContainerIPdu.
    :ivar i_pdu_timing_specifications: The upper multiplicity of this
        role has been increased to * due to resolving an atpVariation
        stereotype. The previous value was 1.
    :ivar i_signal_to_pdu_mappings: The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar pdu_counters: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar pdu_replications: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar unused_bit_pattern: AUTOSAR COM and AUTOSAR IPDUM are filling
        not used areas of an IPDU with this bit-pattern. This attribute
        is mandatory to avoid undefined behavior. This byte-pattern will
        be repeated throughout the IPdu.
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
        name = "I-SIGNAL-I-PDU"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: ISignalIPdu.ShortNameFragments | None = field(
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
    annotations: ISignalIPdu.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    has_dynamic_length: Boolean | None = field(
        default=None,
        metadata={
            "name": "HAS-DYNAMIC-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    length: Integer | None = field(
        default=None,
        metadata={
            "name": "LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    meta_data_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "META-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    contained_i_pdu_props: ContainedIPduProps | None = field(
        default=None,
        metadata={
            "name": "CONTAINED-I-PDU-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_pdu_timing_specifications: ISignalIPdu.IPduTimingSpecifications | None = field(
        default=None,
        metadata={
            "name": "I-PDU-TIMING-SPECIFICATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_signal_to_pdu_mappings: ISignalIPdu.ISignalToPduMappings | None = (
        field(
            default=None,
            metadata={
                "name": "I-SIGNAL-TO-PDU-MAPPINGS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    pdu_counters: ISignalIPdu.PduCounters | None = field(
        default=None,
        metadata={
            "name": "PDU-COUNTERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_replications: ISignalIPdu.PduReplications | None = field(
        default=None,
        metadata={
            "name": "PDU-REPLICATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unused_bit_pattern: Integer | None = field(
        default=None,
        metadata={
            "name": "UNUSED-BIT-PATTERN",
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
    class IPduTimingSpecifications:
        i_pdu_timing: list[IPduTiming] = field(
            default_factory=list,
            metadata={
                "name": "I-PDU-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ISignalToPduMappings:
        i_signal_to_i_pdu_mapping: list[ISignalToIPduMapping] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-TO-I-PDU-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PduCounters:
        signal_i_pdu_counter: list[SignalIPduCounter] = field(
            default_factory=list,
            metadata={
                "name": "SIGNAL-I-PDU-COUNTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class PduReplications:
        signal_i_pdu_replication: list[SignalIPduReplication] = field(
            default_factory=list,
            metadata={
                "name": "SIGNAL-I-PDU-REPLICATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
