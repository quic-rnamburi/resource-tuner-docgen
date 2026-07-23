Quick Start
===========

This guide walks through the minimum steps needed to tune a resource from a client application.

Prerequisites
-------------

- Link your application against ``libUrmClient.so``
- Include the three public headers:

  .. code-block:: c

     #include "UrmAPIs.h"
     #include "UrmPlatformAL.h"

Basic Resource Tuning
---------------------

1. **Build a resource request array** using :c:type:`SysResource`:

   .. code-block:: c

      SysResource resources[2];

      // CPU big cluster — set frequency to performance tier
      resources[0].mResCode = CONSTRUCT_RES_CODE(URM_RES_CPU_BIG_CLUSTER_FREQ, 0, 0);
      resources[0].mValue   = 1800000; // kHz

      // GPU frequency
      resources[1].mResCode = CONSTRUCT_RES_CODE(URM_RES_GPU_FREQ, 0, 0);
      resources[1].mValue   = 650000;  // kHz

2. **Call tuneResources** to apply them and get a handle:

   .. code-block:: c

      int64_t handle = 0;
      int32_t result = tuneResources(resources, 2, &handle,
                                     /*durationMs=*/0, /*pid=*/getpid());
      if (result != 0) {
          // handle error
      }

3. **Release the handle** when done:

   .. code-block:: c

      untuneResources(handle);

Signal Example
--------------

Relay a signal to notify URM of a workload event:

.. code-block:: c

   int64_t sigHandle = 0;
   uint32_t args[] = { MY_APP_WORKLOAD_ID };

   int32_t result = tuneSignal(MY_SIG_ID, MY_SIG_TYPE,
                               sizeof(args)/sizeof(args[0]),
                               args, &sigHandle);
   // ... after workload ends:
   untuneSignal(sigHandle);

Next Steps
----------

- See :doc:`api/client` for the complete API reference.
- See :doc:`guide/requests` for advanced request patterns (priority, duration, re-tune).
- See :doc:`guide/signals` for the full signal taxonomy.
- See :doc:`guide/extensions` to register custom resource callbacks.
