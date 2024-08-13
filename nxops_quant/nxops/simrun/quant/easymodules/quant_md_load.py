# _*_ coding: utf-8 _*_
# @Time: 2024/8/6 11:07
# @Author: LBJ辉
# @File: quant_md_load
# @Project: nxops_quant
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