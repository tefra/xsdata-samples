from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .chapter import Chapter

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwComponentDocumentation:
    """
    This class specifies the ability to write dedicated documentation to a
    component type according to ASAM FSX.

    :ivar sw_feature_def: This element contains the definition of the
        physical functionality of this software component. This
        definition is more or less formal and is intended to be
        delivered from modeling tools.
    :ivar sw_feature_desc: This element contains the textual description
        of the software functionality of this software component. Expert
        should write this description.
    :ivar sw_test_desc: This element contains suggestions and hints for
        the test of the software functionality of this software
        component.
    :ivar sw_calibration_notes: This element contains calibration
        instructions and hints for a calibration engineer.
    :ivar sw_maintenance_notes: This element contains information
        regarding the software maintenance of the component.
    :ivar sw_diagnostics_notes: This element contains general
        information about diagnostics issues within the component.
    :ivar sw_carb_doc: This element records the documentation requested
        by CARB.
    :ivar chapter: These chapters provide additional information about
        the software component that do not fit in the other chapters.
        Note that this is subject to variation because Chapter
        aggregations in the role chapter are variant within the
        documentation in general. The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "SW-COMPONENT-DOCUMENTATION"

    sw_feature_def: Optional[Chapter] = field(
        default=None,
        metadata={
            "name": "SW-FEATURE-DEF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_feature_desc: Optional[Chapter] = field(
        default=None,
        metadata={
            "name": "SW-FEATURE-DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_test_desc: Optional[Chapter] = field(
        default=None,
        metadata={
            "name": "SW-TEST-DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_calibration_notes: Optional[Chapter] = field(
        default=None,
        metadata={
            "name": "SW-CALIBRATION-NOTES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_maintenance_notes: Optional[Chapter] = field(
        default=None,
        metadata={
            "name": "SW-MAINTENANCE-NOTES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_diagnostics_notes: Optional[Chapter] = field(
        default=None,
        metadata={
            "name": "SW-DIAGNOSTICS-NOTES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sw_carb_doc: Optional[Chapter] = field(
        default=None,
        metadata={
            "name": "SW-CARB-DOC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    chapter: list[Chapter] = field(
        default_factory=list,
        metadata={
            "name": "CHAPTER",
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
