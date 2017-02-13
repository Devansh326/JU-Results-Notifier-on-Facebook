import os
import json
import config


SITE_ROOT = os.environ.get('SITE_ROOT', config.SITE_ROOT)
RESULTS_PATH = os.path.join(SITE_ROOT, "PUBLISHED_RESULTS.json")


def clear():
    empty_list = []
    with open(RESULTS_PATH, 'w') as fp:
        json.dump(empty_list, fp, indent=-1)
