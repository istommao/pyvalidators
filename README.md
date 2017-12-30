[![Build Status](https://travis-ci.org/istommao/pyvalidators.svg?branch=master)](https://travis-ci.org/istommao/pyvalidators)
[![codecov](https://codecov.io/gh/istommao/pyvalidators/branch/master/graph/badge.svg)](https://codecov.io/gh/istommao/pyvalidators)
[![PyPI](https://img.shields.io/pypi/v/pyvalidators.svg)](https://pypi.python.org/pypi/pyvalidators)
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg?style=plastic)](https://pypi.python.org/pypi/pyvalidators)

# Common validators use python

## Feature

* phone number validator
* ip address validator
* email address validator
* id card validator

## Install

    pip install pyvalidators


## Simple Usage

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

    >>> from pyvalidators.email import is_valid_email
    >>> is_valid_email('12345@qq.com')
    True
    >>> is_valid_email('1235')
    False

    >>> from pyvalidators.idcard import is_valid_idcard
    >>> is_valid_idcard('220582197707198132')
    True
    >>> is_valid_idcard('1235')
    False
    ...

## Phone validator

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


## Ip address validator

    >>> from pyvalidators.ipaddr import IPAddrValidator
    >>> IPAddrValidator.is_valid('127.0.0.1')
    True
    >>> IPAddrValidator.is_valid('127.0.0.sdf')
    False
    ...

## Email address validator

    >>> from pyvalidators.email import is_valid_email
    >>> is_valid_email('www@gmail.com')
    True
    >>> is_valid_email('@gmail.com')
    False
    ...
