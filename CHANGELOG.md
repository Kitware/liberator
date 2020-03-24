Liberator - static code extractor for Python 
--------------------------------------------

|GitlabCIPipeline| |GitlabCICoverage| |Pypi| |Downloads| 

Liberator is a Python library that "liberates" (i.e. statically extracts) class
/ function source code from an existing python library into a single standalone
module. 

It works by statically parsing the code for the class / function definition and
then recursively parsing and extracting all missing dependencies.


..The main webpage for this project is: https://gitlab.kitware.com/python/liberator


.. |Pypi| image:: https://img.shields.io/pypi/v/liberator.svg
   :target: https://pypi.python.org/pypi/liberator

.. |Downloads| image:: https://img.shields.io/pypi/dm/liberator.svg
   :target: https://pypistats.org/packages/liberator

.. |ReadTheDocs| image:: https://readthedocs.org/projects/liberator/badge/?version=latest
    :target: http://liberator.readthedocs.io/en/latest/

.. # See: https://ci.appveyor.com/project/jon.crall/liberator/settings/badges
.. .. |Appveyor| image:: https://ci.appveyor.com/api/projects/status/py3s2d6tyfjc8lm3/branch/master?svg=true
.. :target: https://ci.appveyor.com/project/jon.crall/liberator/branch/master

.. |GitlabCIPipeline| image:: https://gitlab.kitware.com/python/liberator/badges/master/pipeline.svg
   :target: https://gitlab.kitware.com/python/liberator/-/jobs

.. |GitlabCICoverage| image:: https://gitlab.kitware.com/python/liberator/badges/master/coverage.svg?job=coverage
    :target: https://gitlab.kitware.com/python/liberator/commits/master

