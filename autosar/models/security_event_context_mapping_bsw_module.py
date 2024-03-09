from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .identifier import Identifier
from .idsm_instance_ref_conditional import IdsmInstanceRefConditional
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .security_event_context_props import SecurityEventContextProps
from .security_event_filter_chain_ref_conditional import (
    SecurityEventFilterChainRefConditional,
)
from .short_name_fragment import ShortNameFragment
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SecurityEventContextMappingBswModule:
    """
    This meta-class represents the ability to associate a collection of security
    events with an IdsM instance and with the executional context of a BSW module
    in which this IdsM instance can receive reports for these security events.

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
    :ivar filter_chains: This reference defines the filter chain to be
        applied to each of the referenced security events (depending on
        the reporting mode). This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar idsm_instances: This reference defines the IdsmInstance onto
        which the security events are mapped. This property was modified
        due to atpVariation (DirectedAssociationPattern).
    :ivar mapped_security_events: This aggregation represents (through
        further references) the SecurityEventDefinitions to be mapped to
        an IdsmInstance with additional mapping-dependent properties.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        -1.
    :ivar affected_bsw_module: This attribute is used to identify the
        name of the BSW module in whose executional context a security
        event can occur. The set of BSW module names is standardized by
        AUTOSAR.
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
        name = "SECURITY-EVENT-CONTEXT-MAPPING-BSW-MODULE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "SecurityEventContextMappingBswModule.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional[
        "SecurityEventContextMappingBswModule.Annotations"
    ] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    filter_chains: Optional[
        "SecurityEventContextMappingBswModule.FilterChains"
    ] = field(
        default=None,
        metadata={
            "name": "FILTER-CHAINS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    idsm_instances: Optional[
        "SecurityEventContextMappingBswModule.IdsmInstances"
    ] = field(
        default=None,
        metadata={
            "name": "IDSM-INSTANCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapped_security_events: Optional[
        "SecurityEventContextMappingBswModule.MappedSecurityEvents"
    ] = field(
        default=None,
        metadata={
            "name": "MAPPED-SECURITY-EVENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    affected_bsw_module: Optional[String] = field(
        default=None,
        metadata={
            "name": "AFFECTED-BSW-MODULE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class FilterChains:
        security_event_filter_chain_ref_conditional: List[
            SecurityEventFilterChainRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-FILTER-CHAIN-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class IdsmInstances:
        idsm_instance_ref_conditional: List[IdsmInstanceRefConditional] = (
            field(
                default_factory=list,
                metadata={
                    "name": "IDSM-INSTANCE-REF-CONDITIONAL",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class MappedSecurityEvents:
        security_event_context_props: List[SecurityEventContextProps] = field(
            default_factory=list,
            metadata={
                "name": "SECURITY-EVENT-CONTEXT-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
