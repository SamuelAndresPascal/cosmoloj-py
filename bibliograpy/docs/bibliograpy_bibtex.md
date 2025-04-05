# Bibliograpy Bibtex

```text
usage: bibliograpy bibtex [-h] [--encoding [ENCODING]] [--output-dir [OUTPUT_DIR]] [--output-file [OUTPUT_FILE]] [--scope [SCOPE] | --shared-scope] [--init-scope [INIT_SCOPE]] [file]

positional arguments:
  file                  path to the input bibliography file

options:
  -h, --help            show this help message and exit
  --encoding, -e [ENCODING]
                        the bibliograpy configuration file encoding (default to utf-8)
  --output-dir, -O [OUTPUT_DIR]
                        the source bibliograpy file output directory
  --output-file, -o [OUTPUT_FILE]
                        the source bibliograpy output file name
  --scope, -s [SCOPE]   the scope name, must be consistent with --init-scope (for bibtex format cross-reference resolution)
  --shared-scope, -S    use the default shared scope named SHARED_SCOPE
  --init-scope, -i [INIT_SCOPE]
                        the scope initialization value line (for bibtex format cross-reference resolution)
```
