from dataclasses import dataclass

from sdmx_ml.models.identifiable_type import IdentifiableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TransitionBaseType(IdentifiableType):
    """TransitionBaseType defines the base refinement of the TransitionType.

    Its purpose is to retrict the urn attribute.
    """
