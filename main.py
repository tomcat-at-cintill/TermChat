import requests, os

while True:
    os.system("cls")
    print("TermChat\n\nPlease choose a channel:")
    print(requests.get("https://termchat.t0mcat.repl.co/channels").text.replace(",", "\n")+"\n")
    channel = input("Channel name: ")
    username = input("Username to log in as: ")
    while True:
        os.system("cls")
        print("TermChat\n")
        print(requests.get(f"https://termchat.t0mcat.repl.co/get?channel={channel.lower()}").text)
        print("Choose a command:\nsend\nchangechannel\nreload\nexit\n")
        command = input("> ")
        if command.lower() == "send":
            texttosend = input("Text to send: ")
            requests.post("https://termchat.t0mcat.repl.co/send", data={"username": username, "message": texttosend, "channel": channel.lower()})
        elif command.lower() == "changechannel":
            break
        elif command.lower() == "reload":
            pass
        elif command.lower() == "exit":
            os.system("cls")
            print("Bye!")
            quit()
