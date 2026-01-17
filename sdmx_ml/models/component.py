from dataclasses import dataclass

from sdmx_ml.models.component_type import ComponentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class Component(ComponentType):
    """
    Component is an abstract element that serves as a substitution head for
    all components.

    Concrete instances of this must use a concrete instance of
    ComponentType.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
