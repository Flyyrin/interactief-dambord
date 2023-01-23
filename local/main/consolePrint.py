def consolePrint(text):
    with open('console.txt', 'a') as console:
        console.write(f"{text}\n")