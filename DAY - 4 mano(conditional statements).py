# today we are gonnna do conditional programming
#where specific set of code will execute and certain don't
#it is like real life logic 
# example:if we want something we will buy that but if it doesn't there to buy we will buy an alternate product
#lets imagine a scene where i will buy the mobile if it is under 15k


Samsung = [16000,"GOOD CAMERA","BEST PERFORMANCE","5G NETWORK"]
Redmi = [14000,"BETTER CAMERA","GOOD PERFORMANCE","5G NETWORK"]
Oppo = [13000,"NICE CAMERA","AVERAGE PERFORMANCE","4G NETWORK"]
Buyer_choice = int(input("Enter your budget :"))
His_need = input("What you need?\nGOOD PERFORMANCE\nAVERAGE PERFORMANCE\nBEST PERFORMANCE\n")
if Buyer_choice < 15000 and His_need in Samsung:
    print("he will buy samsung")
elif Buyer_choice < 15000 and His_need in Redmi:
    print("he will buy redmi")
if Buyer_choice < 15000 and His_need in Oppo:
    print("he will buy oppo  ")
