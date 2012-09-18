from distutils.core import setup

setup(
    name = "PySPED-Tools",
    packages = ["pysped_tools"],
    package_data = {'pysped_tools': ['cadeia-certificadora/*', 'schema/*']},
    version = "0.0.1",
    description = "Common library for SPED specifications",
    author = "Daniel Hartmann",
    author_email = "daniel@proge.com.br",
    url = "https://github.com/proge/PySPED-Tools",
    download_url = "https://nodeload.github.com/proge/PySPED-Tools/tarball/v0.0.1",
    keywords = ["sped", "brazil", "brasil"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        ],
    long_description = """\
PySPED Tools
------------

SPED is the Brazilian public system of digital bookkeeping.

This module implements
 - Signature for SSL requests
 - Certificate manipulation
"""
)