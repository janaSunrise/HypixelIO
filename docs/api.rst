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

Client
~~~~~~

.. autoclass:: Client
    :members:
    :undoc-members:


Converters
----------

Converter
~~~~~~~~~

.. autoclass:: Converters
    :members:
    :undoc-members:


Utility
-------

Utils
~~~~~

.. autoclass:: Utils
    :members:
    :undoc-members:

Errors
------

.. autoexception:: hypixelio.exceptions.GuildNotFoundError


.. autoexception:: hypixelio.exceptions.HypixelAPIError


.. autoexception:: hypixelio.exceptions.InvalidArgumentError


.. autoexception:: hypixelio.exceptions.PlayerNotFoundError


.. autoexception:: hypixelio.exceptions.RateLimitError
