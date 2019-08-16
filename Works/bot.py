# --- Define your functions below! ---
def intro(user):
    print("Hello! My name is " + user)
    print("do you want to take a picture with me?")
def DeathSequence(user):
    print("NOOOOOOOOOO")
    print("WHYYYY")
def collission(user):
    print("404 Error")
    print("Mann.exe has stopped working")
def isvalid(input1, input2):
    if(input1 in input2):
        return True


# --- Put your main program below! ---
def main():
  while True:
    how = input("How are you?")
    list = ["good", "bad", "awful", "fine", "great"]
    a = isvalid(how, list)
    print(a)
    user = "Mann"
    intro(user)
    answer = input("Come over here. What do you say?")
    if(answer == ("yes" or "Yes" or "YES")):
        print("Awesome!")
        print("Smile, princess")
        print("Perfect! One more")
        answer = input("Do you like the picture?")
        if(answer == ("yes" or "YES" or "Yes")):
            print("I'm glad")
            print("Of course, you can give me a little something, eh?")
        answer = input("A tip? Hm?")
        if(answer == ("no" or "No" or "NO")):
            print("Oh please, friend! Have a heart!")
            answer = input("Please?")
            if(answer == ("no" or "NO" or "No")):
                print("Oh come on! We've all got to make money somehow!")
                answer == input("Don't you have money? That's fine! The ATM's right over there, let's go together!")
                if(answer != ("yes" or "YES" or "Yes")):
                    print("PISS OFF")
                    print("Mann.exe is down")

    elif(answer == ("no" or "NO" or "No")):
            user = "Mann"
            DeathSequence(user)
            break
    else:
        if(answer != ("no" or "NO" or "No" or "Yes" or "YES" or "yes")):
            user = "Mann"
            collision(user)
            break









# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
