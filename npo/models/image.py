from dataclasses import dataclass
from npo.models.image_type_1 import ImageType1

__NAMESPACE__ = "urn:vpro:shared:2009"


@dataclass
class Image(ImageType1):
    class Meta:
        name = "image"
        namespace = "urn:vpro:shared:2009"
