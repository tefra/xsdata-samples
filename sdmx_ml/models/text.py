from dataclasses import dataclass

from sdmx_ml.models.text_type import TextType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class Text(TextType):
    """
    Text is a reusable element, used for providing a language specific text value
    for general purposes (i.e. not for a name or description).
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"
