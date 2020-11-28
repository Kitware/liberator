Liberator - static code extractor for Python 
--------------------------------------------


## Version 0.0.2 - Unreleased

### Fixed:
* Fixed corner case where name was only given as a prefix of a fully imported module. Fixed this with a `pygtrie.StringTrie`.

### Changed

* Removed 2.7 and 3.5 support
* Slightly better support for unparsing multiline strings 
* Experimental `close2` method
