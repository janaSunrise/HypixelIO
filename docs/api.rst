.. currentmodule:: hypixelio

API Reference
=============

Version Related Info
---------------------

There is a single way to check the version for this library.

.. data:: __version__

    A string representation of the version. e.g. ``'0.1.0b1'``. This is based
    off of :pep:`440`.


Clients
-------

.. autoclass:: Client
    :members:
    :undoc-members:


Converters
----------

.. autoclass:: Converters
    :members:
    :undoc-members:


Utility
-------

.. autoclass:: Utils
    :members:
    :undoc-members:


Async to sync portal
--------------------

.. autoclass:: hypixelio._async.Portal
    :members:
    :undoc-members:

.. autofunction:: hypixelio._async.create_portal
