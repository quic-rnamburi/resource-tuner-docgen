Client API Reference
====================

Header: ``client/APIs/Include/UrmAPIs.h``

This header exposes the core client-facing functions for tuning resources, signalling
workload events, and querying runtime properties.

.. contents::
   :local:
   :depth: 2

Resource Tuning
---------------

.. doxygenfunction:: tuneResources
   :project: URM

.. doxygenfunction:: retuneResources
   :project: URM

.. doxygenfunction:: untuneResources
   :project: URM

Property Query
--------------

.. doxygenfunction:: getProp
   :project: URM

Signal API
----------

.. doxygenfunction:: tuneSignal
   :project: URM

.. doxygenfunction:: relaySignal
   :project: URM

.. doxygenfunction:: untuneSignal
   :project: URM
