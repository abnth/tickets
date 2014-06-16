
=====
Usage
=====

This section contains information, including examples, about how to use
*django-taggit-autocomplete-modified* in your existing Django projects or applications.

Instead of using the default ``TaggableManager`` provided by *django-taggit*,
use the manager provided by *django-taggit-autocomplete-modified*::

    from taggit_autocomplete_modified.managers \
        import TaggableManagerAutocomplete as TaggableManager

