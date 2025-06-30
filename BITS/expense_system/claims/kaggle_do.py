#!/usr/bin/env python3
import pandas as pd
# from claims.models import Center

data = pd.read_excel(args[1], sheet_name="Sheet1")

print(data["Station Name"])
print(data["Station Code"])