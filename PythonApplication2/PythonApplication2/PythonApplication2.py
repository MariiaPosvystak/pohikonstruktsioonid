from datetime import *
from calendar import *
tana=date.today()
print(f"Tere! T�na on {tana}")

# 27/12/2022
tana = tana.strftime("%d/%m/#Y")
print(f"Tere! T�na on {tana}")
paevadekodus=monthrange(2025,1)[1]
print(f"jaanuaris on {paevadekodus} p�eva")
paevad=tana.day 
on j��nud=paevadekodus-paevad
print(f"J��nuaris on j��nud {on j��nud} on j��nud")

# # Decemder 27, 2022
# tana = tana.strftime("%B/%d/#Y")
# print(f"Tere! T�na on {tana}")

# # 12/27/22
# tana = tana.strftime("%m/%d/%y")
# print(f"Tere! T�na on {tana}")

# # Dec-27-2022
# tana = tana.strftime("%b-%d-%Y")
# print(f"Tere! T�na on {tana}")
