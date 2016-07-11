# Common validators use python

* phone number validator
* ip address validator



## phone validator

.. code-block:: python

    >>> from pyvalidators.phone import PhoneValidator
    >>> PhoneValidator.is_valid('18068823333')
    True
    >>> PhoneValidator.is_valid('1068823333')
    False
    ...


## ip address validator

.. code-block:: python

    >>> from pyvalidators.ipaddr import IPAddrValidator
    >>> IPAddrValidator.is_valid('127.0.0.1')
    True
    >>> IPAddrValidator.is_valid('127.0.0.sdf')
    False
    ...
