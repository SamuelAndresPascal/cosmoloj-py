import json
import logging
from argparse import Namespace
from pathlib import Path

import yaml

from bibliograpy.api import Institution

LOG = logging.getLogger(__name__)

def _process(ns: Namespace):
    """config
    """
    LOG.info("dependencies")

    extension = ns.file.split('.')[-1]
    output_dir = Path(Path.cwd(), ns.output)

    LOG.info('open configuration file %s', ns.file)
    with open(ns.file, encoding=ns.encoding) as s:

        if extension == 'yml':
            content = yaml.safe_load(s)
        elif extension == 'json':
            content = json.load(s)
        else:
            raise ValueError(f'unsupported configuration format {extension}')

        with open(Path(output_dir, 'bib.py'), 'w', encoding=ns.encoding) as o:
            o.write('from bibliograpy.api import Institution\n')
            o.write('\n')
            for ref in content:
                ref_type = ref['type']
                if ref_type == 'institution':
                    o.write(f'{Institution.from_dict(ref).to_source_bib()}\n')

