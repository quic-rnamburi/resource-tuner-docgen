Platform Abstraction Types
==========================

Header: ``modula/Common/Include/UrmPlatformAL.h``

This header defines the platform-level types, enums, and macros shared between
client applications and the URM server.

.. contents::
   :local:
   :depth: 2

Core Types
----------

.. doxygenstruct:: SysResource
   :project: URM
   :members:

Enumerations
------------

.. doxygenenum:: RequestPriority
   :project: URM

.. doxygenenum:: Modes
   :project: URM

Resource Code Macros
--------------------

These macros build and decode the 32-bit ``ResCode`` values used in :c:type:`SysResource`.

.. doxygendefine:: CONSTRUCT_RES_CODE
   :project: URM

.. doxygendefine:: SET_REQUEST_PRIORITY
   :project: URM

.. doxygendefine:: ADD_ALLOWED_MODE
   :project: URM

.. doxygendefine:: EXTRACT_REQUEST_PRIORITY
   :project: URM

Resource Code List
------------------

The following resource codes are defined via the ``RES_CODE_LIST`` X-macro:

.. doxygenfile:: UrmPlatformAL.h
   :project: URM
   :sections: define
