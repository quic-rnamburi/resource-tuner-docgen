Overview
========

The **Qualcomm Userspace Resource Manager (URM)** is a system-level framework that enables
client applications to tune hardware resources and manage device behavior based on workload
demands.

Architecture
------------

URM operates as a client-server architecture:

- **Client** — Applications link against ``libUrmClient.so`` and call the public C APIs
  to request resource tuning, signal relay, or property queries.
- **Server** — A background daemon owns the hardware resource scheduling. It processes
  requests from all clients, applies resource configurations, and manages lifecycle events.
- **Extensions** — OEMs and platform owners can inject custom resource callbacks, YAML
  config overrides, and post-processing callbacks at build time via ``Extensions.h``.

Public API Headers
------------------

There are exactly three public headers exposed to client applications:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Header
     - Purpose
   * - ``UrmAPIs.h``
     - Core client API — resource tuning, signal relay, property queries
   * - ``UrmPlatformAL.h``
     - Platform abstraction types — ``SysResource``, enums, resource/signal code macros
   * - ``Extensions.h``
     - Extension interface — register custom applier callbacks and config file overrides

Key Concepts
------------

**Tune Request**
  A request to configure a set of hardware resources for a process or workload.
  Identified by an opaque ``handle`` returned by :c:func:`tuneResources`.
  The caller is responsible for calling :c:func:`untuneResources` when done.

**Signal**
  A discrete event (e.g., launch, touch, rotation) that triggers resource policy changes
  inside URM and its feature modules. Signals are emitted by clients via
  :c:func:`tuneSignal` / :c:func:`relaySignal`.

**Resource Code (ResCode)**
  A 32-bit integer identifying a hardware resource (CPU cluster frequency, GPU frequency,
  memory bandwidth, etc.). Use the ``CONSTRUCT_RES_CODE`` macro from ``UrmPlatformAL.h``
  to build a valid ResCode.

**Modes**
  URM adapts its resource policies based on the device display state (``Modes`` enum):
  screen-on, screen-off, and always-on variants.

Versioning
----------

This documentation covers version **|version|**.
For changes between versions, see the API reference pages which note deprecated and
breaking changes using the ``\deprecated_since`` and ``\breaking_change`` annotations.
