from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .application_primitive_data_type_subtypes_enum import (
    ApplicationPrimitiveDataTypeSubtypesEnum,
)
from .autosar_variable_ref import AutosarVariableRef
from .compu_method_subtypes_enum import CompuMethodSubtypesEnum
from .data_constr_subtypes_enum import DataConstrSubtypesEnum
from .float_mod import Float
from .integer_value_variation_point import IntegerValueVariationPoint
from .mc_data_instance_subtypes_enum import McDataInstanceSubtypesEnum
from .monotony_enum import MonotonyEnum
from .ref import Ref
from .sw_axis_generic import SwAxisGeneric
from .unit_subtypes_enum import UnitSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwAxisIndividual:
    """
    This meta-class describes an axis integrated into a parameter (field
    etc.).

    The integration makes this individual to each parameter. The so-called
    grouped axis represents the counterpart to this. It is conceived as an
    independent parameter (see class SwAxisGrouped).

    :ivar max_gradient: This attribute defines the maximum permissible
        gradient for an adjustable object (curve, map or cuboid) with
        respect to a specific axis. MaxGrad  =  maximum( absolute((Value
        i,k - Value i-1,k)/(Axis Point i - Axis Point i-1)) )
    :ivar monotony: This attribute specifies the monotony constraint for
        an adjustable object (curve, map or cuboid) with respect to a
        specific axis. This information can be used by MCD  system to
        verify whether the monotony constraint is fulfilled and to
        prevent from changes violating the constraint.
    :ivar input_variable_type_ref: This is the datatype of the input
        value for the axis. This allows to define e.g. a type of curve,
        where the input value is finalized at the access point.
    :ivar sw_variable_refs: Refers to input variables of the axis. It is
        possible to specify more than one variable. Here the following
        is valid: * The variable with the highest priority shall be
        given first. It is used in the generation of the code and is
        also displayed first in the application system. * All variables
        referenced shall be of the same physical nature. This is usually
        detected in that the conversion formulae affected refer back to
        the same SI-units. In AUTOSAR this ensured by the constraint,
        that the referenced input variables shall use a type compatible
        to "inputVariableType". * This multiple referencing allows a
        base point distribution for more than one input variable to be
        used. One example of this are the temperature curves which can
        depend both on the induction air temperature and the engine
        temperature. These variables can be displayed simultaneously by
        MCD systems (adjustment systems), enabling operating points to
        be shown in the curves.
    :ivar compu_method_ref: This is the compuMethod which is expected
        for the axis. It is used in early stages if the particular
        input-value is not yet available.
    :ivar unit_ref: This represents the physical unit of the input value
        of the axis. It is provided to support the case that the
        particular input variable is not yet known.
    :ivar sw_max_axis_points: Maximum number of base points contained in
        the axis of a map or curve.
    :ivar sw_min_axis_points: Minimum number of base points contained in
        the axis of a map or curve.
    :ivar data_constr_ref: Refers to constraints, e.g. for plausibility
        checks.
    :ivar sw_axis_generic: this specifies the properties of a generic
        axis if applicable.
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
        name = "SW-AXIS-INDIVIDUAL"

    max_gradient: Float | None = field(
        default=None,
        metadata={
            "name": "MAX-GRADIENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    monotony: MonotonyEnum | None = field(
        default=None,
        metadata={
            "name": "MONOTONY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    input_variable_type_ref: SwAxisIndividual.InputVariableTypeRef | None = field(
        default=None,
        metadata={
            "name": "INPUT-VARIABLE-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_variable_refs: SwAxisIndividual.SwVariableRefs | None = field(
        default=None,
        metadata={
            "name": "SW-VARIABLE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    compu_method_ref: SwAxisIndividual.CompuMethodRef | None = field(
        default=None,
        metadata={
            "name": "COMPU-METHOD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    unit_ref: SwAxisIndividual.UnitRef | None = field(
        default=None,
        metadata={
            "name": "UNIT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_max_axis_points: IntegerValueVariationPoint | None = field(
        default=None,
        metadata={
            "name": "SW-MAX-AXIS-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_min_axis_points: IntegerValueVariationPoint | None = field(
        default=None,
        metadata={
            "name": "SW-MIN-AXIS-POINTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    data_constr_ref: SwAxisIndividual.DataConstrRef | None = field(
        default=None,
        metadata={
            "name": "DATA-CONSTR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_axis_generic: SwAxisGeneric | None = field(
        default=None,
        metadata={
            "name": "SW-AXIS-GENERIC",
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

    @dataclass
    class InputVariableTypeRef(Ref):
        dest: ApplicationPrimitiveDataTypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SwVariableRefs:
        """
        :ivar autosar_variable: This represents the reference to a
            Variable in an Autosar system. Note that the target of the
            reference within AutosarVariableRef shall be typed by a
            primitive data type
        :ivar mc_data_instance_var_ref: This reference is used in the
            McSupport file to express the final instance of input values
            etc. It is not allowed to use this outside of an
            McDataInstance. The referenced mcDataInstance shall be
            originated from a VariableDataPrototype.
        """

        autosar_variable: list[AutosarVariableRef] = field(
            default_factory=list,
            metadata={
                "name": "AUTOSAR-VARIABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "sequence": 1,
            },
        )
        mc_data_instance_var_ref: list[
            SwAxisIndividual.SwVariableRefs.McDataInstanceVarRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "MC-DATA-INSTANCE-VAR-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "sequence": 1,
            },
        )

        @dataclass
        class McDataInstanceVarRef(Ref):
            dest: McDataInstanceSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class CompuMethodRef(Ref):
        dest: CompuMethodSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class UnitRef(Ref):
        dest: UnitSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class DataConstrRef(Ref):
        dest: DataConstrSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
