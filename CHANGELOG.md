# dataset ChangeLog

*The changelog has only been started with version 0.3.12, previous
changes must be reconstructed from revision history.*

* 0.3.15: dataset Databases can now have customized row types.
  This allows, for example, information to be retrieved in 
  attribute-accessible dict subclasses, such as stuf.
* 0.3.14: dataset went viral somehow. Thanks to @gtsafas for
  refactorings, @alasdairnicol for fixing the Freezfile example in 
  the documentation. @diegoguimaraes fixed the behaviour of insert to
  return the newly-created primary key ID. table.find_one() now
  returns a dict, not an SQLAlchemy ResultProxy. Slugs are now generated
  using the Python-Slugify package, removing slug code from dataset. 
* 0.3.13: Fixed logging, added support for transformations on result
  rows to support slug generation in output (#28).
* 0.3.12: Makes table primary key's types and names configurable, fixing
  #19. Contributed by @dnatag.
