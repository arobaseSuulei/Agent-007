def main():
    while True:
        input_user=input("> ")
        print(f"You said {input_user}")
        if(input_user in ("exit","q")):
            print("Bye.")
            break



if __name__=="__main__":
    main()