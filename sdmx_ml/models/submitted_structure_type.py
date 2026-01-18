from dataclasses import dataclass, field

from sdmx_ml.models.action_type import ActionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubmittedStructureType:
    """
    SubmittedStructureType generally references a submitted structural
    object.

    When used in a submit structure request, its purpose is to override the
    default action or external dependency resolution behavior. If neither
    of these indicators are set, then it will be ignored. In a submit
    structure response, it is used to reference a submitted object for the
    purpose of providing a status for the submission. In this case, the
    action attribute should be populated in order to echo the requested
    action.

    :ivar maintainable_object:
    :ivar action: The action attribute will indicate the action to be
        taken on the referenced structural object. This should be
        provided when this structure is used in a submit structure
        response.
    :ivar external_dependencies: The externalDependencies attribute
        should be set to true if the repository is expected to use
        external reference URLs in the structural components to retrieve
        objects on which the referenced object has dependencies. (Thus,
        if a data structure referenced here is being submitted to the
        repository, and the structure message has URLs which point to
        the locations of the codelists it uses, then this attribute
        should be set to true). This should not be provided when this
        structure is used in a submit structure response.
    """

    maintainable_object: str | None = field(
        default=None,
        metadata={
            "name": "MaintainableObject",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
            "pattern": r".+\)",
        },
    )
    action: ActionType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    external_dependencies: bool | None = field(
        default=None,
        metadata={
            "name": "externalDependencies",
            "type": "Attribute",
        },
    )
