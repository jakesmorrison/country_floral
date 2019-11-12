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

    ZIPCODES = {
        'Nampa': {
            '83651': 8.00,
            '83652': 8.00,
            '83653': 8.00,
            '83686': 8.00,
            '83687': 8.00,
        },
        'Caldwell': {
            '83605': 12.00,
            '83606': 12.00,
            '83607': 12.00,
            '83651': 12.00
        },
        'Kuna': {
            '83634': 20.00,
            '83642': 20.00,
            '83687': 20.00,
        },
        'Melba': {
            '83641': 20.00
        },
        'Marsing': {
            '83639': 20.00,
        },
        'Middleton': {
            '83644': 20.00,
        },
        'Meridian': {
            '83646': 12.00,
            '83642': 12.00,
        },        
        'Star': {
            '83669': 15.00,
        },
        'Eagle': {
            '83616': 20.00,
        },
    }
