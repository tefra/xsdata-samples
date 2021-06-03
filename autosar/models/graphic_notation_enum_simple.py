from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class GraphicNotationEnumSimple(Enum):
    """
    :cvar BMP: bitmap image
    :cvar EPS: Encapsulated Postscript
    :cvar GIF: Graphics Interchange Format
    :cvar JPG: "Joint Photographic Experts Group"  format
    :cvar PDF: Portable Document Format
    :cvar PNG: Portable Network Graphics
    :cvar SVG: scalable vector graphic
    :cvar TIFF: Tagged Image File Format
    """
    BMP = "BMP"
    EPS = "EPS"
    GIF = "GIF"
    JPG = "JPG"
    PDF = "PDF"
    PNG = "PNG"
    SVG = "SVG"
    TIFF = "TIFF"
