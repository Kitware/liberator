Liberator - static code extractor for Python
--------------------------------------------

|GitlabCIPipeline| |GitlabCICoverage| |ReadTheDocs| |Pypi| |Downloads|

+---------------+---------------------------------------------+
| Github        | https://gitlab.kitware.com/python/liberator |
+---------------+---------------------------------------------+
| Pypi          | https://pypi.org/project/liberator          |
+---------------+---------------------------------------------+
| ReadTheDocs   | https://liberator.readthedocs.io/en/latest/ |
+---------------+---------------------------------------------+

Liberator is a Python library that "liberates" (i.e. statically extracts) class
/ function source code from an existing python library into a single standalone
module.

It works by statically parsing the code for the class / function definition and
then recursively parsing and extracting all missing dependencies.

Here is an example. Say that you want to use the ``find_exe`` function from
``ubelt``, but you don't want to depend on ubelt itself, you can extract the
minimal code necessary to define the ``find_exe`` function in a new standalone
module via:


.. code:: python

    # Create a Liberator instance to manage construction of
    # the new standalone code.
    from liberator.core import Liberator
    lib = Liberator()

    # Pass the liberator object the function you want to expose
    # You can add more than one function this way.
    import ubelt as ub
    lib.add_dynamic(ub.find_exe)

    # Tell liberator about the library that you dont want to depend on,
    # any (statically findable) external references to that library will be
    # vendored into the new liberated code.
    lib.expand(['ubelt'])

    # Finally access the "current source code" which will
    # have the self-contained version of the "liberated" utility.
    print(lib.current_sourcecode())


Limitations
~~~~~~~~~~~

Liberator has several limitations. It only works if the code is expressed
statically (i.e. no decorators that register methods in a list to be injected
into something later).  It does not do any work to evaluate anything, it just
looks at function definitions and pulls them in verbatim.  It also does no work
to mangle to deconflict different functions with the same names (although it
could and that is an extension I'd lke add).  Lastly, it can only "expand"
packages imported at the top level of the code. Nested imports are not
"liberated". This is another extension that could be implemented, but it
currently isn't.



.. |Pypi| image:: https://img.shields.io/pypi/v/liberator.svg
   :target: https://pypi.python.org/pypi/liberator

.. |Downloads| image:: https://img.shields.io/pypi/dm/liberator.svg
   :target: https://pypistats.org/packages/liberator

.. # See: https://ci.appveyor.com/project/jon.crall/liberator/settings/badges
.. .. |Appveyor| image:: https://ci.appveyor.com/api/projects/status/py3s2d6tyfjc8lm3/branch/main?svg=true
.. :target: https://ci.appveyor.com/project/jon.crall/liberator/branch/main

.. |GitlabCIPipeline| image:: https://gitlab.kitware.com/python/liberator/badges/main/pipeline.svg
   :target: https://gitlab.kitware.com/python/liberator/-/jobs

.. |GitlabCICoverage| image:: https://gitlab.kitware.com/python/liberator/badges/main/coverage.svg?job=coverage
    :target: https://gitlab.kitware.com/python/liberator/commits/main

.. |ReadTheDocs| image:: https://readthedocs.org/projects/liberator/badge/?version=latest
    :target: http://liberator.readthedocs.io/en/latest/
