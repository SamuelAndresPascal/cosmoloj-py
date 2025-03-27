# Bibliograpy process

```text
usage: bibliograpy process [-h] [--encoding [ENCODING]] [--output-dir [OUTPUT_DIR]] [--output-file [OUTPUT_FILE]] [--format [FORMAT]] [--scope [SCOPE]] [--init-scope [INIT_SCOPE]] [file]

positional arguments:
  file                  path to the bibliograpy configuration file

options:
  -h, --help            show this help message and exit
  --encoding, -e [ENCODING]
                        the bibliograpy configuration file encoding (default to utf-8)
  --output-dir, -O [OUTPUT_DIR]
                        the source bibliograpy file output directory
  --output-file, -o [OUTPUT_FILE]
                        the source bibliograpy output file name
  --format, -f [FORMAT]
                        the input bibliography format (bib, bibtex, ris2001)
  --scope, -s [SCOPE]   the scope name, must be consistent with --init-scope (for bibtex format cross-reference resolution)
  --init-scope, -S [INIT_SCOPE]
                        the scope import line (for bibtex format cross-reference resolution)
```
