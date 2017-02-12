import os
import config

VALIDATION_STRINGS = os.environ.get('VALIDATION_STRINGS', config.VALIDATION_STRINGS)


def check_results(html):
    out = True
    for s in VALIDATION_STRINGS:
        out = (s in html)and(out)

    return out