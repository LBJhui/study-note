# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-21 11:22:11
@LastEditTime : 2020-08-12 14:34:10
@LastEditors  : yi.mt
@Description  : 
'''

import base64
import rapidjson

from nxpy.context import AppContext

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.Hash import SHA

class EasyCipher():
    def __init__(self, public_key, private_key):
        super().__init__()

        self.public_key = public_key
        self.private_key = private_key

    def public_encrypt(self, data):
        encrypt_rsa = PKCS1_v1_5.new(self.public_key)
        data = data if isinstance(data, bytes) else bytes(data, encoding="UTF-8")
        encrypted_data = encrypt_rsa.encrypt(data)
        base64_text = base64.b64encode(encrypted_data).decode("UTF-8")
        return base64_text

    def private_encrypt(self, data):
        encrypt_rsa = PKCS1_v1_5.new(self.private_key)
        data = data if isinstance(data, bytes) else bytes(data, encoding="UTF-8")
        encrypted_data = encrypt_rsa.encrypt(data)
        base64_text = base64.b64encode(encrypted_data).decode("UTF-8")
        return base64_text

    def private_decrypt(self, data):
        decrypt_rsa = PKCS1_v1_5.new(self.private_key)
        data = data if isinstance(data, bytes) else base64.b64decode(data)
        sentinel = Random.new().read(15 + SHA.digest_size)
        decrypted_text = decrypt_rsa.decrypt(data, sentinel).decode("UTF-8")
        return decrypted_text


class EasyCipherUtils():
    ciphers = {}

    @classmethod
    def load_ciphers(cls, config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)
            for (cipher_id, cipher_config) in config.items():
                public_key = cls.load_public_key(AppContext.get_config_path(cipher_config["public"]))
                private_key = cls.load_private_key(AppContext.get_config_path(cipher_config["private"]), cipher_config.get("password"))

                cls.ciphers.update({cipher_id: EasyCipher(public_key, private_key)})

    @classmethod
    def get_cipher(cls, id):
        return cls.ciphers.get(id)

    @staticmethod
    def gen_rsa_key(bits=2048):
        key = RSA.generate(bits)
        return key

    @staticmethod
    def load_public_key(key_file):
        key = None
        with open(key_file, "rb") as pkf:
            key = RSA.import_key(pkf.read())
        return key

    @staticmethod
    def load_private_key(key_file, password=None):
        key = None
        with open(key_file, "rb") as pkf:
            key = RSA.import_key(pkf.read(), passphrase=password)
        return key

    @staticmethod
    def serialize(key, public_key_file, private_key_file, password=None):
        with open(public_key_file, "wb") as pkf:
            pkf.write(key.publickey().export_key())
        with open(private_key_file, "wb") as pkf:
            pkf.write(key.export_key(passphrase=password))

    @staticmethod
    def symmetric_encrypt(data, key, iv=None):
        key = bytes(key, encoding="UTF-8")
        key = pad(key, AES.block_size) if len(key) % AES.block_size != 0 else key

        cipher = None
        if iv:
            iv = bytes(iv, encoding="UTF-8")
            iv = pad(iv, AES.block_size) if len(iv) % AES.block_size != 0 else iv
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
        else:
            cipher = AES.new(key, AES.MODE_ECB)
            
        data = data if isinstance(data, bytes) else bytes(data, encoding="UTF-8")
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))
        base64_text = base64.b64encode(encrypted_data).decode("UTF-8")
        return base64_text

    @staticmethod
    def symmetric_decrypt(data, key, iv=None):
        key = bytes(key, encoding="UTF-8")
        key = pad(key, AES.block_size) if len(key) % AES.block_size != 0 else key

        cipher = None
        if iv:
            iv = bytes(iv, encoding="UTF-8")
            iv = pad(iv, AES.block_size) if len(iv) % AES.block_size != 0 else iv
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
        else:
            cipher = AES.new(key, AES.MODE_ECB)

        data = data if isinstance(data, bytes) else base64.b64decode(data)
        decrypted_data = unpad(cipher.decrypt(data), AES.block_size)
        decrypted_text = decrypted_data.decode("UTF-8")
        return decrypted_text


if __name__ == "__main__":
    #rsa_key = EasyCryptoUtils.gen_rsa_key()
    #EasyCryptoUtils.serialize(rsa_key, "./config/data_public.pem", "./config/data_private.pem", "password")
    #public_key = rsa_key.publickey()
    #private_key = rsa_key
    public_key = EasyCipherUtils.load_public_key("./config/data_public.pem")
    private_key = EasyCipherUtils.load_private_key("./config/data_private.pem", "password")

    cipher = EasyCipher(public_key, private_key)


    def public_encrypt():
        a = cipher.public_encrypt("1234567812345678")
        print(a)

    import timeit
    print(timeit.timeit("public_encrypt()", setup="from __main__ import public_encrypt",number=20))

    a = cipher.public_encrypt("1234567812345678")
    print(a)
    a = cipher.private_decrypt(a)
    print(a)

    a = EasyCipherUtils.symmetric_encrypt("""{"userID":"admin","password":"","verificationCode":""}""", "tSbBgPhB33wTGaK7f80ade69f9da40b8")
    print(a)
    a = EasyCipherUtils.symmetric_decrypt(a, "tSbBgPhB33wTGaK7f80ade69f9da40b8")
    print(a)
    a = EasyCipherUtils.symmetric_decrypt("vA4iAFLsqEGQMrzf+1uduhYoIN6T3g69Clf/1MCm62OyR5f3cewhjx6gvCOOzoKcAHunFRK8JqqX722t/m2Eyg==", "351oRUjnwvRMuLJcde46788b38f3406d")
    print(a)

