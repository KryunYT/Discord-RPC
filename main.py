from pypresence import Presence
import time

client_id = "1349759901957881907"  
RPC = Presence(client_id)
RPC.connect()  


RPC.update(
    details="🤖 Coding right now",  
    state="In MinecraftCheat",    
    large_image="ai_logo",          
    buttons=[{"label": "Donate", "url": "https://www.donationalerts.com/r/kryun"}]
)

print("Close the programm Ctrl+C.")


while True:
    time.sleep(15)  
