from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CommunicationsTransportMethodEnumeration(Enum):
    HTTP_POST = "httpPost"
    OTHER = "other"
    WSDL_SOAP = "wsdlSoap"
    WSDL_SOAP_DOCUMENT_LITERAL = "wsdlSoapDocumentLiteral"
    HTTP_URL_JSON = "httpUrlJSON"
    HTTP_URL_PROTO_BUFFERS = "httpUrlProtoBuffers"
