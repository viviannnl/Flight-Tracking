from api import fetcher

def main_wrapper():
    print(f"Hi this is the start. The name is {main_wrapper.__name__}")
    fetcher.states_accessor()

    print("This is the end")

if __name__ == "__main__":
    main_wrapper()