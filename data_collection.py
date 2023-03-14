#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:13:38 2023

@author: yugosaito
"""

import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/yugosaito/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs("data scientist", 15, False, path, 15)

print(df)