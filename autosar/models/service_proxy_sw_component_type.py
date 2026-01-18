from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .blueprint_policy_list import BlueprintPolicyList
from .blueprint_policy_not_modifiable import BlueprintPolicyNotModifiable
from .blueprint_policy_single import BlueprintPolicySingle
from .category_string import CategoryString
from .consistency_needs import ConsistencyNeeds
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .p_port_prototype import PPortPrototype
from .port_group import PortGroup
from .pr_port_prototype import PrPortPrototype
from .r_port_prototype import RPortPrototype
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String
from .sw_component_documentation import SwComponentDocumentation
from .swc_internal_behavior import SwcInternalBehavior
from .symbol_props import SymbolProps
from .unit_group_subtypes_enum import UnitGroupSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ServiceProxySwComponentType:
    """
    This class provides the ability to express a software-component which
    provides access to an internal service for remote ECUs.

    It acts as a proxy for the service providing access to the service. An
    important use case is the request of vehicle mode switches: Such
    requests can be communicated via sender-receiver interfaces across ECU
    boundaries, but the mode manager being responsible to perform the mode
    switches is an AUTOSAR Service which is located in the Basic Software
    and is not visible in the VFB view. To handle this situation, a
    ServiceProxySwComponentType will act as proxy for the mode manager. It
    will have R-Ports to be connected with the mode requestors on VFB level
    and Service-Ports to be connected with the local mode manager at ECU
    integration time. Apart from the semantics, a
    ServiceProxySwComponentType has these specific properties: * A
    prototype of it can be mapped to more than one ECUs in the system
    description. * Exactly one additional instance of it will be created in
    the ECU-Extract per ECU to which the prototype has been mapped. * For
    remote communication, it can have only R-Ports with sender-receiver
    interfaces and 1:n semantics. * There shall be no connectors between
    two prototypes of any ServiceProxySwComponentType.

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
    :ivar blueprint_policys: This role indicates whether the
        blueprintable element will be modifiable or not motifiable.
    :ivar short_name_pattern: This attribute represents the pattern
        which shall be used to build the shortName of the derived
        elements. As of now it is modeled as a String.  In general it
        should follow the pattern: pattern = (placeholder | namePart)*
        placeholder = "{" namePart "}" namePart = identifier | "_" This
        is subject to be refined in subsequent versions. Note that this
        is marked as obsolete. Use the xml attribute namePattern instead
        as it applies to Identifier and CIdentifier (shortName, symbol
        etc.)
    :ivar sw_component_documentations: This adds a documentation to the
        SwComponentType. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was 1.
    :ivar consistency_needss: This represents the collection of
        ConsistencyNeeds owned by the enclosing SwComponentType. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar ports: The PortPrototypes through which this SwComponentType
        can communicate. The aggregation of PortPrototype is subject to
        variability with the purpose to support the conditional
        existence of PortPrototypes. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar port_groups: A port group being part of this component. The
        upper multiplicity of this role has been increased to * due to
        resolving an atpVariation stereotype. The previous value was -1.
    :ivar unit_group_refs: This allows for the specification of which
        UnitGroups are relevant in the context of referencing
        SwComponentType.
    :ivar internal_behaviors: The SwcInternalBehaviors owned by an
        AtomicSwComponentType can be located in a different physical
        file. Therefore the aggregation is &lt;&lt;atpSplitable&gt;&gt;.
        The upper multiplicity of this role has been increased to * due
        to resolving an atpVariation stereotype. The previous value was
        1.
    :ivar symbol_props: This represents the SymbolProps for the
        AtomicSwComponentType.
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
        name = "SERVICE-PROXY-SW-COMPONENT-TYPE"

    short_name: Identifier = field(
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: (
        None | ServiceProxySwComponentType.ShortNameFragments
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
    annotations: None | ServiceProxySwComponentType.Annotations = field(
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
    blueprint_policys: None | ServiceProxySwComponentType.BlueprintPolicys = (
        field(
            default=None,
            metadata={
                "name": "BLUEPRINT-POLICYS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    short_name_pattern: None | String = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_component_documentations: (
        None | ServiceProxySwComponentType.SwComponentDocumentations
    ) = field(
        default=None,
        metadata={
            "name": "SW-COMPONENT-DOCUMENTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    consistency_needss: (
        None | ServiceProxySwComponentType.ConsistencyNeedss
    ) = field(
        default=None,
        metadata={
            "name": "CONSISTENCY-NEEDSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ports: None | ServiceProxySwComponentType.Ports = field(
        default=None,
        metadata={
            "name": "PORTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    port_groups: None | ServiceProxySwComponentType.PortGroups = field(
        default=None,
        metadata={
            "name": "PORT-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unit_group_refs: None | ServiceProxySwComponentType.UnitGroupRefs = field(
        default=None,
        metadata={
            "name": "UNIT-GROUP-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    internal_behaviors: (
        None | ServiceProxySwComponentType.InternalBehaviors
    ) = field(
        default=None,
        metadata={
            "name": "INTERNAL-BEHAVIORS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    symbol_props: None | SymbolProps = field(
        default=None,
        metadata={
            "name": "SYMBOL-PROPS",
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
    class BlueprintPolicys:
        blueprint_policy_list: list[BlueprintPolicyList] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-LIST",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        blueprint_policy_not_modifiable: list[BlueprintPolicyNotModifiable] = (
            field(
                default_factory=list,
                metadata={
                    "name": "BLUEPRINT-POLICY-NOT-MODIFIABLE",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        blueprint_policy_single: list[BlueprintPolicySingle] = field(
            default_factory=list,
            metadata={
                "name": "BLUEPRINT-POLICY-SINGLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class SwComponentDocumentations:
        sw_component_documentation: list[SwComponentDocumentation] = field(
            default_factory=list,
            metadata={
                "name": "SW-COMPONENT-DOCUMENTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class ConsistencyNeedss:
        consistency_needs: list[ConsistencyNeeds] = field(
            default_factory=list,
            metadata={
                "name": "CONSISTENCY-NEEDS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class Ports:
        p_port_prototype: list[PPortPrototype] = field(
            default_factory=list,
            metadata={
                "name": "P-PORT-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        pr_port_prototype: list[PrPortPrototype] = field(
            default_factory=list,
            metadata={
                "name": "PR-PORT-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        r_port_prototype: list[RPortPrototype] = field(
            default_factory=list,
            metadata={
                "name": "R-PORT-PROTOTYPE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class PortGroups:
        port_group: list[PortGroup] = field(
            default_factory=list,
            metadata={
                "name": "PORT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class UnitGroupRefs:
        unit_group_ref: list[
            ServiceProxySwComponentType.UnitGroupRefs.UnitGroupRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "UNIT-GROUP-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass(kw_only=True)
        class UnitGroupRef(Ref):
            dest: UnitGroupSubtypesEnum = field(
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass(kw_only=True)
    class InternalBehaviors:
        swc_internal_behavior: list[SwcInternalBehavior] = field(
            default_factory=list,
            metadata={
                "name": "SWC-INTERNAL-BEHAVIOR",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
