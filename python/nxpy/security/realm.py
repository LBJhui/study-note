# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 16:45
# @Author: LBJ辉
# @File: realm
# @Project: python
import uuid


class Securable:
    def __init__(self, secure_id=uuid.uuid4().kex):
        super().__init__()
