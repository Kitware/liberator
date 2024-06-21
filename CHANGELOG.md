Liberator - static code extractor for Python 
--------------------------------------------

## Version 0.1.0 - Unreleased

### Removed

* Drop 3.6 and 3.7 support



## Version 0.0.3 - Released 2023-08-22

### Fixed
* assignments with type annotations
* docstr formatting

### Changed
* Removed python2 cruft


## Version 0.0.2 - Released 2022-12-10

### Fixed:
* Fixed corner case where name was only given as a prefix of a fully imported module. Fixed this with a `pygtrie.StringTrie`.

### Changed

* Removed 2.7 and 3.5 support
* Slightly better support for unparsing multiline strings 
* Experimental `close2` method

* Nested imports are now extracted and logged (useful for maintaining
  dependencies)
