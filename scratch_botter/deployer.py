from BotCode import bot

def deployBots():
    url = input("Input Project URL: \n")
    print("\n")
    while True:
        try:
            amount = int(input("How many bots?: \n"))
            #amount = 1
            break
        except ValueError:
            print("Enter a valid number")
    for nums in range(amount):
        print(f"Bot Number {nums+1}")
        bot(url)
if (__name__=='__main__'):
    deployBots()