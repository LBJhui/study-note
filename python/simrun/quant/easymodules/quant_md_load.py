# _*_ coding: utf-8 _*_
# @Time: 2024/8/14 14:00
# @Author: LBJ辉
# @File: quant_md_load
# @Project: python

alias = "QuantMdLoad"

realm = {
    "roles": {},
    "rules": {
    }
}

ware = {
    "clean_quant_rightissue": {
        "sql": """DELETE FROM quant.t_quantrightissue"""
    }
}
