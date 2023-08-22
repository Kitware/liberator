Liberator - static code extractor for Python 
--------------------------------------------


## Version 0.0.3 - Unreleased

### Fixed
* assignments with type annotations


## Version 0.0.2 - Released 2022-12-10

### Fixed:
* Fixed corner case where name was only given as a prefix of a fully imported module. Fixed this with a `pygtrie.StringTrie`.

### Changed

* Removed 2.7 and 3.5 support
* Slightly better support for unparsing multiline strings 
* Experimental `close2` method

* Nested imports are now extracted and logged (useful for maintaining
  dependencies)
