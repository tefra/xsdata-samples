from dataclasses import dataclass

from sdmx_ml.models.text_type import TextType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class Description(TextType):
    """
    Description is a reusable element, used for providing a longer human-readable
    description of an object.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"
