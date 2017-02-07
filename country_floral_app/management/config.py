import collections
class CONFIG(object):
    KEYWORDS = {
        "flowers": "roses lilies daisies peony anemomes hyacinths daffodils carnations snapdragons peas helleborus hydrangea alstromeria sunflowers larkspur asters agapanthus amaranthus hydrangea gerbera".split(" "),
        "colors": "pink red orange yellow green violet blue cherry ".split(" "),
        "mood": "happy somber sad congratulatory apology mourning celebratory fun bright unique sweet whimsical".split(" "),
        "seasons": "spring summer fall winter mix".split(" "),
        "occasion": "valentines,christmas,mothers day,fathers day,memorial day,birthday".split(","),
        "style": "modern,contemporary,rich,colorful,tones".split(","),
        "other": " ".split(" "),
    }
    BASE_DEL_FEE = 6
