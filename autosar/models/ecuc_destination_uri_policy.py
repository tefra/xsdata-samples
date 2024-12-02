from dataclasses import dataclass, field
from typing import Optional

from .ecuc_add_info_param_def import EcucAddInfoParamDef
from .ecuc_boolean_param_def import EcucBooleanParamDef
from .ecuc_choice_container_def import (
    EcucChoiceContainerDef,
    EcucParamConfContainerDef,
)
from .ecuc_choice_reference_def import EcucChoiceReferenceDef
from .ecuc_destination_uri_nesting_contract_enum import (
    EcucDestinationUriNestingContractEnum,
)
from .ecuc_enumeration_param_def import EcucEnumerationParamDef
from .ecuc_float_param_def import EcucFloatParamDef
from .ecuc_foreign_reference_def import EcucForeignReferenceDef
from .ecuc_function_name_def import EcucFunctionNameDef
from .ecuc_instance_reference_def import EcucInstanceReferenceDef
from .ecuc_integer_param_def import EcucIntegerParamDef
from .ecuc_linker_symbol_def import EcucLinkerSymbolDef
from .ecuc_multiline_string_param_def import EcucMultilineStringParamDef
from .ecuc_reference_def import EcucReferenceDef
from .ecuc_string_param_def import EcucStringParamDef
from .ecuc_symbolic_name_reference_def import EcucSymbolicNameReferenceDef
from .ecuc_uri_reference_def import EcucUriReferenceDef

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucDestinationUriPolicy:
    """The EcucDestinationUriPolicy describes the EcucContainerDef that will be
    targeted by EcucUriReferenceDefs.

    The type of the description is dependent of the
    destinationUriNestingContract attribute.

    :ivar containers: Description of the targetContainer in case that
        the destinationUriNestingPolicy is set to targetContainer. In
        all other cases the subContainers of the target container are
        defined here.
    :ivar destination_uri_nesting_contract: This attribute defines how
        the referenced target EcucContainerDef is described.
    :ivar parameters: Description of parameters that are contained in
        the target container.
    :ivar references: Description of references that are contained in
        the target container.
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
        name = "ECUC-DESTINATION-URI-POLICY"

    containers: Optional["EcucDestinationUriPolicy.Containers"] = field(
        default=None,
        metadata={
            "name": "CONTAINERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    destination_uri_nesting_contract: Optional[
        EcucDestinationUriNestingContractEnum
    ] = field(
        default=None,
        metadata={
            "name": "DESTINATION-URI-NESTING-CONTRACT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    parameters: Optional["EcucDestinationUriPolicy.Parameters"] = field(
        default=None,
        metadata={
            "name": "PARAMETERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    references: Optional["EcucDestinationUriPolicy.References"] = field(
        default=None,
        metadata={
            "name": "REFERENCES",
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

    @dataclass
    class Containers:
        ecuc_choice_container_def: list[EcucChoiceContainerDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-CHOICE-CONTAINER-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_param_conf_container_def: list[EcucParamConfContainerDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-PARAM-CONF-CONTAINER-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Parameters:
        ecuc_add_info_param_def: list[EcucAddInfoParamDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-ADD-INFO-PARAM-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_boolean_param_def: list[EcucBooleanParamDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-BOOLEAN-PARAM-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_enumeration_param_def: list[EcucEnumerationParamDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-ENUMERATION-PARAM-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_float_param_def: list[EcucFloatParamDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-FLOAT-PARAM-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_function_name_def: list[EcucFunctionNameDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-FUNCTION-NAME-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_integer_param_def: list[EcucIntegerParamDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-INTEGER-PARAM-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_linker_symbol_def: list[EcucLinkerSymbolDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-LINKER-SYMBOL-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_multiline_string_param_def: list[EcucMultilineStringParamDef] = (
            field(
                default_factory=list,
                metadata={
                    "name": "ECUC-MULTILINE-STRING-PARAM-DEF",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
        ecuc_string_param_def: list[EcucStringParamDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-STRING-PARAM-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class References:
        ecuc_choice_reference_def: list[EcucChoiceReferenceDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-CHOICE-REFERENCE-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_foreign_reference_def: list[EcucForeignReferenceDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-FOREIGN-REFERENCE-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_instance_reference_def: list[EcucInstanceReferenceDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-INSTANCE-REFERENCE-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_reference_def: list[EcucReferenceDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-REFERENCE-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_symbolic_name_reference_def: list[
            EcucSymbolicNameReferenceDef
        ] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-SYMBOLIC-NAME-REFERENCE-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ecuc_uri_reference_def: list[EcucUriReferenceDef] = field(
            default_factory=list,
            metadata={
                "name": "ECUC-URI-REFERENCE-DEF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
