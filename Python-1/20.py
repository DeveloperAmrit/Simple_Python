print("Please don't type the meassage by tour own.Paste it after clicking enter")
a = input("Paste your meassage to be checked\n")

if a.count("Congratulations!") >0 or a.count("Congratulations")>0 or a.count("buy now")>0 or a.count("BUY NOW")>0 or a.count("Buy now")>0 or a.count("Buy Now")>0 or a.count("buy now!")>0 or a.count("BUY NOW!")>0 or a.count("Buy now!")>0 or a.count("Buy Now!")>0 or a.count("Subscribe now")>0 or  a.count("Subscribe now!")>0 or a.count("SUBSCRIBE NOW")>0 :
    print("This is a SCAM meassage")
else:
    print("This is safe")