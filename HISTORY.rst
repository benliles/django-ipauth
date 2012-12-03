0.4.1 (2012/12/03)
------------------

* Added logging to backend and login view

0.4 (2012/11/27)
----------------

* Fixed validation bugs in Range
* Made range collision validation errors more verbose

0.3 (2012/10/22)
----------------

* Fixed a validation bug for IPAddressFormField

0.2 (2011/06/23)
----------------

* Made the upper end of the range optional
* Fixed a bug in the Range model clean method if upper is null

0.1 (2011/06/17)
----------------

* IPAddressFormField for inputting IP Addresses
* IPAddressModelField for storing IP addresses as integers (so math works)
* Range Model for storing IP Ranges tied to a user account
* Range Authentication backend
* A login view wrapper that attempts to login via IP first
