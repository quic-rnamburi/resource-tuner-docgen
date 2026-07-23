Extensions API Reference
========================

Header: ``extensions/Include/Extensions.h``

The Extensions interface allows OEMs and platform integrators to customize URM behavior
at build time: registering custom resource applier/teardown callbacks, overriding
configuration YAML files, and registering post-processing callbacks.

.. note::

   Extension macros must be used in the **global scope** of a translation unit.
   They rely on static initialization to register callbacks before ``main()``.

.. contents::
   :local:
   :depth: 2

Extension Class
---------------

.. doxygenclass:: Extensions
   :project: URM
   :members:

Data Types
----------

.. doxygenstruct:: PostProcessCBData
   :project: URM
   :members:

.. doxygenenum:: ConfigType
   :project: URM

Registration Macros
-------------------

.. doxygendefine:: URM_REGISTER_RES_APPLIER_CB
   :project: URM

.. doxygendefine:: URM_REGISTER_RES_TEAR_CB
   :project: URM

.. doxygendefine:: URM_REGISTER_CONFIG
   :project: URM

.. doxygendefine:: URM_REGISTER_POST_PROCESS_CB
   :project: URM
