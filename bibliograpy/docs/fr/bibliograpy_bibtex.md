# Bibliograpy Bibtex

```text
usage: bibliograpy bibtex [-h] [--encoding [ENCODING]] [--output-dir [OUTPUT_DIR]] [--output-file [OUTPUT_FILE]] [--scope [SCOPE] | --shared-scope] [--init-scope [INIT_SCOPE]] [file]

positional arguments:
  file                  path to the input bibliography file (default to bibliography.bib)

options:
  -h, --help            show this help message and exit
  --encoding, -e [ENCODING]
                        the bibliograpy configuration file encoding (default to utf-8)
  --output-dir, -O [OUTPUT_DIR]
                        the source bibliograpy file output directory (default to .)
  --output-file, -o [OUTPUT_FILE]
                        the source bibliograpy output file name (default to bibliography.py)
  --scope, -s [SCOPE]   the local scope name
  --shared-scope, -S    use the bibtex bibliograpy shared scope named SHARED_SCOPE
  --init-scope, -i [INIT_SCOPE]
                        the local scope initialization (default to "{}")
```
