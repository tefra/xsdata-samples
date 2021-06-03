from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.documentation_subtypes_enum import DocumentationSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.sdg_def_subtypes_enum import SdgDefSubtypesEnum
from autosar.models.string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Baseline:
    """Specification of the baseline of the AUTOSAR standard this Data Exchange
    Point relates to.

    The baseline is specified by listing the AUTOSAR products and their
    revisions. Custom defined functionality and deviations to the
    standard can be provided as well. All references to specification
    elements in this Data Exchange Point refer to specification elements
    that are part of this specification baseline.

    :ivar standard_revisions:
    :ivar custom_specification_refs: Reference tof custom specifications
        that extend this baseline,
    :ivar custom_sdg_def_refs: Reference to custom SdgDefs that extend
        the data format of this baseline,
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
        name = "BASELINE"

    standard_revisions: Optional["Baseline.StandardRevisions"] = field(
        default=None,
        metadata={
            "name": "STANDARD-REVISIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    custom_specification_refs: Optional["Baseline.CustomSpecificationRefs"] = field(
        default=None,
        metadata={
            "name": "CUSTOM-SPECIFICATION-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    custom_sdg_def_refs: Optional["Baseline.CustomSdgDefRefs"] = field(
        default=None,
        metadata={
            "name": "CUSTOM-SDG-DEF-REFS",
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
    class StandardRevisions:
        """
        :ivar standard_revision: Specifies a combination of revisions of
            AUTOSAR standards that are used as the specification
            baseline of this Data Exchange Point. All standard
            specification elements that are referenced by this Profile
            of Data Exchange Point have to be part of specifications
            that belong to the defined AUTOSAR standards.
        """
        standard_revision: List[String] = field(
            default_factory=list,
            metadata={
                "name": "STANDARD-REVISION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class CustomSpecificationRefs:
        custom_specification_ref: List["Baseline.CustomSpecificationRefs.CustomSpecificationRef"] = field(
            default_factory=list,
            metadata={
                "name": "CUSTOM-SPECIFICATION-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class CustomSpecificationRef(Ref):
            dest: Optional[DocumentationSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class CustomSdgDefRefs:
        custom_sdg_def_ref: List["Baseline.CustomSdgDefRefs.CustomSdgDefRef"] = field(
            default_factory=list,
            metadata={
                "name": "CUSTOM-SDG-DEF-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class CustomSdgDefRef(Ref):
            dest: Optional[SdgDefSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
