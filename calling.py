#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:07:57 2019

@author: mann
"""

from twilio.rest import Client

account_sid = "ACC_SID"
auth_token = "TOKEN"
client = Client(account_sid, auth_token)

call = client.calls.create(
        record=True,
        to="TO_STRING_NUMBER",
        from_="YOUR TWILIO",
        url="SERVER URL"
        )


