from npo.models.broadcaster_type import BroadcasterType
from npo.models.image_type_2 import ImageType2
from npo.models.image_type_enum import ImageTypeEnum
from npo.models.page_facets_result_type import PageFacetsResultType
from npo.models.page_search_result import PageSearchResult
from npo.models.page_type import PageType
from npo.models.page_type_enum import PageTypeEnum
from npo.models.portal_type import PortalType
from npo.models.result_type import ResultType
from npo.models.search_result_item import SearchResultItem
from npo.models.total_qualifier import TotalQualifier
from xsdata.models.datatype import XmlDateTime


obj = PageSearchResult(
    items=ResultType.Items(
        item=[
            SearchResultItem(
                result=PageType(
                    crid=[
                        "crid://vpro/media/vprobroadcast/WO_VPRO_2297327",
                    ],
                    broadcaster=[
                        BroadcasterType(
                            id="VPRO"
                        ),
                    ],
                    portal=PortalType(
                        name="www.vprobroadcast.com",
                        id="VPROBROADCAST",
                        url="https://www.vprobroadcast.com"
                    ),
                    title="Antibiotics",
                    images=PageType.Images(
                        image=[
                            ImageType2(
                                title="Antibiotica",
                                description="Labyrint",
                                type_value=ImageTypeEnum.PICTURE,
                                url="https://images.poms.omroep.nl/image/s360/665086.jpg"
                            ),
                        ]
                    ),
                    url="https://www.vprobroadcast.com/play~WO_VPRO_2297327~antibiotics~.html",
                    type_value=PageTypeEnum.VIDEO,
                    creation_date=XmlDateTime(2019, 11, 22, 14, 15, 9, 443000000, 60),
                    last_modified=XmlDateTime(2019, 11, 22, 14, 15, 9, 443000000, 60),
                    last_published=XmlDateTime(2019, 11, 22, 14, 15, 24, 341000000, 60),
                    publish_start=XmlDateTime(2015, 10, 16, 14, 23, 14, 729000000, 120),
                    ref_count=0,
                    sort_date=XmlDateTime(2015, 10, 16, 14, 23, 14, 729000000, 120)
                ),
                score=0.3099519
            ),
        ]
    ),
    total=432,
    total_qualifier=TotalQualifier.EQUAL_TO,
    offset=0,
    max=0,
    facets=PageFacetsResultType(

    ),
    selected_facets=PageFacetsResultType(

    )
)
