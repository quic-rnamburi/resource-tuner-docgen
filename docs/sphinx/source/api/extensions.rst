Extensions API Reference
========================

Header: ``extensions/Include/Extensions.h``

Interface for customizing URM behavior at build time: registering custom
resource applier/teardown callbacks, overriding configuration YAML files,
and registering post-processing callbacks.

.. note::

   Extension macros must be used in the **global scope** of a translation unit.
   They rely on static initialization to register callbacks before ``main()``.

.. doxygenfile:: Extensions.h
   :project: URM
