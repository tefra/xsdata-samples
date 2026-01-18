from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.hotel_property import HotelProperty
from travelport.models.permitted_providers_1 import PermittedProviders1
from travelport.models.type_requested_image_size import TypeRequestedImageSize

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class HotelMediaLinksReq(BaseReq1):
    """
    Retrieves all image links from the Galileo Web Services Image Viewer
    eBL for up to 20 properties.

    Only the attributes of the HotelProperty are used in this request.

    Parameters
    ----------
    permitted_providers
    hotel_property
    secure_links
        Request URLs returned use secured site (https) references. Default
        is true
    size_code
        Requested image size. Default is to get ALL images
    rich_media
        Request the Rich Media link. Default is true
    gallery
        Request the Image Gallery link. Default is true
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    permitted_providers: None | PermittedProviders1 = field(
        default=None,
        metadata={
            "name": "PermittedProviders",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    hotel_property: list[HotelProperty] = field(
        default_factory=list,
        metadata={
            "name": "HotelProperty",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 20,
        },
    )
    secure_links: bool = field(
        default=True,
        metadata={
            "name": "SecureLinks",
            "type": "Attribute",
        },
    )
    size_code: TypeRequestedImageSize = field(
        default=TypeRequestedImageSize.A,
        metadata={
            "name": "SizeCode",
            "type": "Attribute",
        },
    )
    rich_media: bool = field(
        default=True,
        metadata={
            "name": "RichMedia",
            "type": "Attribute",
        },
    )
    gallery: bool = field(
        default=True,
        metadata={
            "name": "Gallery",
            "type": "Attribute",
        },
    )
