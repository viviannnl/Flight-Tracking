from api import utils

def main_wrapper():
    print(f"Hi this is the start. The name is {main_wrapper.__name__}")
    utils.solid_example_1(example_param_1="a", example_param_2=1)

    print("This is the end")

if __name__ == "__main__":
    main_wrapper()