from dataclasses import dataclass, field
from typing import List, Optional
from .mc_data_instance import McDataInstance
from .mc_sw_emulation_method_support import McSwEmulationMethodSupport
from .ref import Ref
from .rpt_support_data import RptSupportData
from .sw_systemconstant_value_set_subtypes_enum import (
    SwSystemconstantValueSetSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class McSupportData:
    """Root element for all measurement and calibration support data related to one
    Implementation artifact on an ECU.

    There shall be one such element related to the RTE implementation
    (if it owns MC data) and a separate one for each module or
    component, which owns private MC data.

    :ivar emulation_supports: Describes the calibration method used by
        the RTE. This information is not needed for A2L generation, but
        to setup software emulation in the ECU. The upper multiplicity
        of this role has been increased to * due to resolving an
        atpVariation stereotype. The previous value was -1.
    :ivar mc_parameter_instances: A data instance to be used for
        calibration. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar mc_variable_instances: A data instance to be used for
        measurement. The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar measurable_system_constant_values_refs: Sets of system
        constant values to be transferred to the MCD system, because the
        system constants have been specified with "swCalibrationAccess"
        = readonly.
    :ivar rpt_support_data: The rapid prototyping support data belonging
        to this implementation. The aggregtion is
        &lt;&lt;atpSplitable&gt;&gt; because in case of an already
        exisiting BSW Implementation model, this description will be
        added later in the process, namely at code generation time.
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
        name = "MC-SUPPORT-DATA"

    emulation_supports: Optional["McSupportData.EmulationSupports"] = field(
        default=None,
        metadata={
            "name": "EMULATION-SUPPORTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_parameter_instances: Optional[
        "McSupportData.McParameterInstances"
    ] = field(
        default=None,
        metadata={
            "name": "MC-PARAMETER-INSTANCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_variable_instances: Optional[
        "McSupportData.McVariableInstances"
    ] = field(
        default=None,
        metadata={
            "name": "MC-VARIABLE-INSTANCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    measurable_system_constant_values_refs: Optional[
        "McSupportData.MeasurableSystemConstantValuesRefs"
    ] = field(
        default=None,
        metadata={
            "name": "MEASURABLE-SYSTEM-CONSTANT-VALUES-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_support_data: Optional[RptSupportData] = field(
        default=None,
        metadata={
            "name": "RPT-SUPPORT-DATA",
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
    class EmulationSupports:
        mc_sw_emulation_method_support: List[
            McSwEmulationMethodSupport
        ] = field(
            default_factory=list,
            metadata={
                "name": "MC-SW-EMULATION-METHOD-SUPPORT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class McParameterInstances:
        mc_data_instance: List[McDataInstance] = field(
            default_factory=list,
            metadata={
                "name": "MC-DATA-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class McVariableInstances:
        mc_data_instance: List[McDataInstance] = field(
            default_factory=list,
            metadata={
                "name": "MC-DATA-INSTANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class MeasurableSystemConstantValuesRefs:
        measurable_system_constant_values_ref: List[
            "McSupportData.MeasurableSystemConstantValuesRefs.MeasurableSystemConstantValuesRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "MEASURABLE-SYSTEM-CONSTANT-VALUES-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class MeasurableSystemConstantValuesRef(Ref):
            dest: Optional[SwSystemconstantValueSetSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
