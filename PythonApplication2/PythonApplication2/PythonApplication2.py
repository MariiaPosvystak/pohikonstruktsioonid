from datetime import *
from calendar import *
tana=date.today()
print(f"Tere! Täna on {tana}")

# 27/12/2022
tana = tana.strftime("%d/%m/#Y")
print(f"Tere! Täna on {tana}")
paevadekodus=monthrange(2025,1)[1]
print(f"jaanuaris on {paevadekodus} päeva")
paevad=tana.day 
on jäänud=paevadekodus-paevad
print(f"Jäänuaris on jäänud {on jäänud} on jäänud")

# # Decemder 27, 2022
# tana = tana.strftime("%B/%d/#Y")
# print(f"Tere! Täna on {tana}")

# # 12/27/22
# tana = tana.strftime("%m/%d/%y")
# print(f"Tere! Täna on {tana}")

# # Dec-27-2022
# tana = tana.strftime("%b-%d-%Y")
# print(f"Tere! Täna on {tana}")
