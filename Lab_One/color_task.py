import random

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[94m'
COLOR_BLUE = '\033[93m'
COLOR_END = '\033[0m'

def test():
    color_shades = [COLOR_RED, COLOR_GREEN, COLOR_YELLOW, COLOR_BLUE]
    colors = ['RED', 'GREEN', 'YELLOW', 'BLUE']
    
    num_trial = 5
    correct = 0
    
    print("Welcome to the color game!!!")
    
    for i in range(num_trial):
        word = random.choice(colors)
        ink_color = random.choice(colors)
        
        ink_color_code = color_shades[colors.index(ink_color)]

        print(f"The word is: {ink_color_code} {word}")
        print(COLOR_END)
        
        color_input = input("Enter the color of the text:").strip().upper()
        
        if color_input == ink_color:
            print("correct")
            correct += 1
        else:
            print(f"Wrong attempt the answer was {ink_color}")
            
    print(f"You have got:{correct} out of {num_trial}")
            
if __name__ == "__main__":
    test()
