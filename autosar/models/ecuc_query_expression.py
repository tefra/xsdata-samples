from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.ecuc_definition_element_subtypes_enum import EcucDefinitionElementSubtypesEnum
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EcucQueryExpression:
    """Defines a query expression to the ECUC Description and output the result
    as an numerical value.

    Due to the "mixedString" nature of the formula there can be several
    EcuQueryExpressions used.

    :ivar content:
    :ivar config_element_def_global_ref: The EcucQueryExpression points
        to an EcucDefinitionElement that is used to find an element in
        the EcucDescription. In order to find the right element in the
        EcucDescription a search is necessary. If the complete
        EcucDescription needs to be searched this global reference shall
        be used. Due to the "mixedString" nature of the
        EcucQueryExpression several references to EcucDefintionElements
        can be used in one EcucQueryExpression.
    :ivar config_element_def_local_ref: The EcucQueryExpression points
        to an EcucDefinitionElement that is used to find an element in
        the EcucDescription. In order to find the right element in the
        EcucDescription a search is necessary. If the search is executed
        inside of the same module that contains the EcucQuery this local
        reference shall be used. Due to the "mixedString" nature of the
        EcucQueryExpression several references to EcucDefintionElements
        can be used in one EcucQueryExpression.
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
        name = "ECUC-QUERY-EXPRESSION"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    config_element_def_global_ref: List["EcucQueryExpression.ConfigElementDefGlobalRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONFIG-ELEMENT-DEF-GLOBAL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    config_element_def_local_ref: List["EcucQueryExpression.ConfigElementDefLocalRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONFIG-ELEMENT-DEF-LOCAL-REF",
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

    @dataclass
    class ConfigElementDefGlobalRef(Ref):
        dest: Optional[EcucDefinitionElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ConfigElementDefLocalRef(Ref):
        dest: Optional[EcucDefinitionElementSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
