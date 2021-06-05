from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.identifier import Identifier
from autosar.models.mc_parameter_element_group import McParameterElementGroup
from autosar.models.ref import Ref
from autosar.models.variable_data_prototype_subtypes_enum import VariableDataPrototypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class McSwEmulationMethodSupport:
    """This denotes the method used by the RTE to handle the calibration data.
    It is published by the RTE generator and can be used e.g. to generate the
    corresponding emulation method in a Complex Driver. According to the actual
    method given by the category attribute,  not all attributes are always
    needed:

    * double pointered method: only baseReference is mandatory
    * single pointered method: only referenceTable is mandatory
    * initRam method: only elementGroup(s) are mandatory
    Note: For single/double pointered method the group locations are implicitly accessed via the reference table and their location can be found from the initial values in the M1 model of the respective pointers. Therefore, the description of elementGroups is not needed in these cases.  Likewise, for double pointered method the reference table description can be accessed via the M1 model under baseReference.

    :ivar short_label: Assigns a name to this element.
    :ivar category: Identifies the actual method. The possible names
        shall correspond to the symbols of the ECU configuration
        parameter for the calibration method of the RTE, and can include
        vendor specific methods.
    :ivar base_reference_ref: Refers to the base pointer in case of the
        double-pointered method.
    :ivar element_groups: Denotes the grouping of calibration parameters
        in the actual RTE code. Depending on the category, this
        information maybe required to set up the emulation code.
    :ivar reference_table_ref: Refers to the pointer table in case of
        the single-pointered method.
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
        name = "MC-SW-EMULATION-METHOD-SUPPORT"

    short_label: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    base_reference_ref: Optional["McSwEmulationMethodSupport.BaseReferenceRef"] = field(
        default=None,
        metadata={
            "name": "BASE-REFERENCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    element_groups: Optional["McSwEmulationMethodSupport.ElementGroups"] = field(
        default=None,
        metadata={
            "name": "ELEMENT-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    reference_table_ref: Optional["McSwEmulationMethodSupport.ReferenceTableRef"] = field(
        default=None,
        metadata={
            "name": "REFERENCE-TABLE-REF",
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
    class BaseReferenceRef(Ref):
        dest: Optional[VariableDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ElementGroups:
        mc_parameter_element_group: List[McParameterElementGroup] = field(
            default_factory=list,
            metadata={
                "name": "MC-PARAMETER-ELEMENT-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class ReferenceTableRef(Ref):
        dest: Optional[VariableDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
