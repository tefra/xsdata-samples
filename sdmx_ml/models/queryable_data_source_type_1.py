from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class QueryableDataSourceType1:
    """
    QueryableDataSourceType describes a data source which is accepts an
    standard SDMX Query message and responds appropriately.

    :ivar data_url: DataURL contains the URL of the data source.
    :ivar wsdlurl: WSDLURL provides the location of a WSDL instance on
        the internet which describes the queryable data source.
    :ivar wadlurl: WADLURL provides the location of a WADL instance on
        the internet which describes the REST protocol of the queryable
        data source.
    :ivar is_restdatasource: The isRESTDatasource attribute indicates,
        if true, that the queryable data source is accessible via the
        REST protocol.
    :ivar is_web_service_datasource: The isWebServiceDatasource
        attribute indicates, if true, that the queryable data source is
        accessible via Web Services protocols.
    """

    class Meta:
        name = "QueryableDataSourceType"

    data_url: str | None = field(
        default=None,
        metadata={
            "name": "DataURL",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
            "required": True,
        },
    )
    wsdlurl: str | None = field(
        default=None,
        metadata={
            "name": "WSDLURL",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    wadlurl: str | None = field(
        default=None,
        metadata={
            "name": "WADLURL",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    is_restdatasource: bool | None = field(
        default=None,
        metadata={
            "name": "isRESTDatasource",
            "type": "Attribute",
            "required": True,
        },
    )
    is_web_service_datasource: bool | None = field(
        default=None,
        metadata={
            "name": "isWebServiceDatasource",
            "type": "Attribute",
            "required": True,
        },
    )
