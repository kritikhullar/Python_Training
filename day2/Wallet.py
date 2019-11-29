def createWallet(bal,username):
	ubal=bal
	u_username=username
	def Deposit(amt1):
		nonlocal ubal,u_username
		ubal += amt1
		print("After Depositing:"+ str(amt1) +" , New balance of "+u_username+" is : "+str(ubal))

	def Spend(amt):
		nonlocal ubal,u_username
		if ubal>amt:
			ubal-=amt
			print("Spending: "+ str(amt) +" New balance of "+u_username+" is : "+str(ubal))
		else:
			print("Low on balance")

	def Showbal():
		nonlocal ubal,u_username
		print("Balance of "+u_username+" : "+str(ubal))

	def Transfer(wal,amt):
		nonlocal ubal
		nonlocal u_username
		if amt <= ubal:
			ubal =ubal-amt
			var1 =wal
			var1["Deposit"](amt)
			print("Deducted Amount of "+u_username+" : " + str(amt) + " Balance: "+str(ubal))

	out = {"Deposit":Deposit,"Spend":Spend,"Showbal":Showbal,"Transfer":Transfer}
	return out

out1 = createWallet(10000,"Kriti")
out2 =createWallet(20000,"Sayon")
out2["Transfer"](createWallet(600,"Rahul"),400)
out2["Showbal"]()
out1["Deposit"](200)
out1["Spend"](1000)
out1["Showbal"]()


'''

    out = {"deposit": deposit, "spending": spending, "savings": savings, "transfer": transfer }
    
    return out


out1 = wallet(1000)
out2 = wallet(500)

out1["transfer"](wallet(400), 500)
out1["savings"]()
out1["deposit"](400)
out1["spending"](90)
out1["savings"]()'''