=============
API Reference
=============

Base classes
============

.. autoclass:: TextVault.Encryptor
    :members:
    :undoc-members:
    :member-order: bysource

.. autoclass:: TextVault.Key
    :members:
    :special-members: __init__, __repr__
    :undoc-members:
    :member-order: bysource

-------------------------------------------

.. _kanpsack_api:

Knapsack Encryption Module
==========================

:ref:`Usage <knapsack_usage>`

.. autoclass:: TextVault.KnapsackEncryptor
    :members:
    :member-order: bysource
.. autoclass:: TextVault.KnapsackKey
    :members:
    :member-order: bysource

Example
-------
.. code-block:: python

    # After `$ pip install TextVault`

    from TextVault import KnapsackEncryptor
    txt = "Hello, World!"
    enc = KnapsackEncryptor()

    pub, priv = enc.newkey()
    encrypted = enc.encrypt(txt, pub)
    decrypted = enc.decrypt(encrypted, priv)

    print("Public key:", pub)
    print("Private key:", priv)

    print("Original:", txt)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

----------------------------------------------

RSA Encryption Module
=====================
.. autoclass:: TextVault.RsaEncryptor
    :members:
    :undoc-members:
    :member-order: bysource

----------------------------------------------

Vigenère Encryption Module
==========================
.. autoclass:: TextVault.VigenereEncryptor
    :members:
    :undoc-members:
    :member-order: bysource

----------------------------------------------

JMatrix Encryption Module
==========================
.. autoclass:: TextVault.JMatrixEncryptor
    :members:
    :undoc-members:
    :member-order: bysource
.. autoclass:: TextVault.JMatrixKey
    :members:
    :special-members: __init__
    :undoc-members:
    :member-order: bysource