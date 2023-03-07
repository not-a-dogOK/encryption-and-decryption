# RSA:
This Python file contains a simple implementation of the RSA encryption and decryption algorithm.

## Encryption:
The encryption formula used is:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/072606d75d31af7b625c573d1514f120a49258df" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:15.311ex; height:2.343ex;" alt="{\displaystyle {\boldsymbol {c=m^{e}{\mbox{ mod }}n}}}">
where m is the plaintext message, e is a randomly generated co-prime integer to n, and n is the product of two large prime numbers, p and q.

## Decryption:
The decryption formula used is:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/a592a031a75d3b8ddf7679cfc2c29f8f94f31051" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:15.987ex; height:2.676ex;" alt="{\displaystyle \ {\boldsymbol {m=c^{d}{\mbox{ mod }}n}}}">
where c is the encrypted message, d is the private key generated using p and q and e, and n is the product of the same two prime numbers used for encryption.
