from dataclasses import dataclass, field
from typing import Optional, Tuple, Union

from sdmx_ml.models.action_type import ActionType
from sdmx_ml.models.structures import Structures
from sdmx_ml.models.submitted_structure_type import SubmittedStructureType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubmitStructureRequestType1:
    """SubmitStructureRequestType describes the structure of a structure
    submission.

    Structural components are provided either in-line or referenced via
    a SDMX-ML Structure message external to the registry. A default
    action and external reference resolution action are all provided for
    each of the contained components, but can be overridden on a per
    component basis.

    :ivar structure_location_or_structures:
    :ivar submitted_structure: SubmittedStructure contains a reference
        to one of the structural maintainable artefacts detailed in the
        external SDMX-ML Structure message or in-line and provides an
        override for the default action. This should only be used if the
        action to be performed on the referenced structural object is
        different than the default action. For example, one may want to
        append all structural components of a structure message, save
        one codelist. This codelist could be referenced in a submitted
        structure element and given an action of Informational.
    :ivar action: The action attribute indicates the default action
        (append-add, replace-update, delete, or no action-informational)
        to be taken on all structural components in either the external
        SDMX-ML Structure message or the in-line components. The default
        action is Append. The Replace action is not applicable to final
        structures in the repository, and will produce an error
        condition, as these can be versioned but not modified. To submit
        a later version of a structural object, the object should
        include the incremented version number.
    :ivar external_dependencies: The externalDependencies attribute
        indicates the default resolution of external dependencies. This
        should be set to true if the repository is expected to use
        external reference URLs in the structural components to retrieve
        any externally referenced objects that is used by a non-external
        object.
    """

    class Meta:
        name = "SubmitStructureRequestType"

    structure_location_or_structures: Optional[Union[str, Structures]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StructureLocation",
                    "type": str,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Structures",
                    "type": Structures,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    submitted_structure: Tuple[SubmittedStructureType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubmittedStructure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
        },
    )
    action: ActionType = field(
        default=ActionType.APPEND,
        metadata={
            "type": "Attribute",
        },
    )
    external_dependencies: bool = field(
        default=False,
        metadata={
            "name": "externalDependencies",
            "type": "Attribute",
        },
    )
