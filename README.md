# Common validators use python

* phone number validator
* ip address validator

## install

    pip install pyvalidators


## simple useage

    >>> from pyvalidators.phone import is_valid_phone
    >>> is_valid_phone('18068823333')
    True
    >>> is_valid_phone('1068823333')
    False
    ...

    >>> from pyvalidators.ipaddr import is_valid_ipaddr
    >>> is_valid_ipaddr('127.0.0.1')
    True
    >>> is_valid_ipaddr('127.0.0.sdf')
    False
    ...

## phone validator

    >>> from pyvalidators.phone import PhoneValidator
    >>> PhoneValidator.is_valid('18068823333')
    True
    >>> PhoneValidator.is_valid('1068823333')
    False
    >>> PhoneValidator.number_segment('188002333')
    '无效的号码'
    >>> PhoneValidator.number_segment('15868823333')
    '中国移动'
    >>> PhoneValidator.number_segment('18068823333')
    '中国电信'
    >>> PhoneValidator.number_segment('13068823333')
    '中国联通'
    ...


## ip address validator

    >>> from pyvalidators.ipaddr import IPAddrValidator
    >>> IPAddrValidator.is_valid('127.0.0.1')
    True
    >>> IPAddrValidator.is_valid('127.0.0.sdf')
    False
    ...
