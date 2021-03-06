=========
ccxt-lite
=========

A light-weighted python wrapper of the ccxt library. Specially focused on historical information retrieval, 
in particular, OHLCV and Limit OrderBook Data.

--------------
Base Reference
--------------

This wrapper is built on top of the `ccxt`_, hence the base functionality must be consulted there, the functions provided here are wrapped to make them more user-friendly purposefully for historical information retrieval. Credits to contributors for that particular repository which I think is great as it is, just too confusing for a more mainstream type of user.

.. _ccxt: https://github.com/ccxt/ccxt

------------
Installation
------------

- Cloning repository
  
Clone entire github project

    git@github.com:IteraCapital/ccxt-lite.git

(optional) create a virtual environment

    virtualenv venv

(optional) activate virtual environment

        source ~/venv/bin/activate

and then install dependencies

        pip install -r requirements.txt

------
Author
------

J.Francisco Munnoz - `IFFranciscoME`_ - Is an Associate Professor in the Mathematics and Physics Department, at `ITESO`_ University.

.. _ITESO: https://iteso.mx/
.. _IFFranciscoME: https://iffranciscome.com/

-------
License
-------

**GNU General Public License v3.0** 

*Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license notices 
must be preserved. Contributors provide an express grant of patent rights.*

*Contact: For more information in reggards of this project, please contact francisco.me@iteso.mx*
