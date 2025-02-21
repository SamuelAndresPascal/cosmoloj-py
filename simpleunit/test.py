from setuptools_scm import get_version, Configuration, _get_version

version = get_version(root='..', relative_to=__file__)
print(version)

conf = Configuration.from_file('pyproject.toml')
print(conf)
maybe_version = _get_version(conf, force_write_version_files=True)
print(maybe_version)
