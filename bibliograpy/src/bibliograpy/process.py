"""
bibliograpy process module
"""
import json
import logging
from argparse import Namespace
from pathlib import Path

import yaml

from bibliograpy.api import Misc, TechReport, Unpublished, Proceedings, Article, Book, Booklet, Inbook, Conference, \
    Manual, Mastersthesis, Incollection, Inproceedings, Phdthesis

LOG = logging.getLogger(__name__)

def _process(ns: Namespace):
    """config
    """
    LOG.info("dependencies")

    in_extension = ns.file.split('.')[-1]
    output_dir = Path(Path.cwd(), ns.output)
    output_file = ns.output_file
    out_extension = output_file.split('.')[-1]

    LOG.info('open configuration file %s', ns.file)
    with open(ns.file, encoding=ns.encoding) as s:

        if in_extension == 'yml':
            content = yaml.safe_load(s)
        elif in_extension == 'json':
            content = json.load(s)
        else:
            raise ValueError(f'unsupported configuration format {in_extension}')

        with open(Path(output_dir, output_file), 'w', encoding=ns.encoding) as o:
            if out_extension == 'py':
                o.write('from bibliograpy.api import NonStandard, Article, Book, Booklet, Inbook, Incollection, Inproceedings, Conference, Manual, Mastersthesis, Misc, Phdthesis, Proceedings, TechReport, Unpublished\n')
                o.write('\n')
                for ref in content:
                    ref_type = ref['entry_type']
                    if ref_type == 'article':
                        o.write(f'{Article.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'book':
                        o.write(f'{Book.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'booklet':
                        o.write(f'{Booklet.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'inbook':
                        o.write(f'{Inbook.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'incollection':
                        o.write(f'{Incollection.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'inproceedings':
                        o.write(f'{Inproceedings.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'conference':
                        o.write(f'{Conference.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'manual':
                        o.write(f'{Manual.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'mastersthesis':
                        o.write(f'{Mastersthesis.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'misc':
                        o.write(f'{Misc.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'phdthesis':
                        o.write(f'{Phdthesis.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'proceedings':
                        o.write(f'{Proceedings.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'techreport':
                        o.write(f'{TechReport.from_dict(ref).to_source_bib()}\n')
                    elif ref_type == 'unpublished':
                        o.write(f'{Unpublished.from_dict(ref).to_source_bib()}\n')
            elif out_extension in ['yml', 'yaml']:
                yaml.dump(content, o, sort_keys=False)
