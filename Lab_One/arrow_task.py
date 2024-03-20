
import random
import time
diction = {">":"L", "<":"R"}
given_time = 5

def arrow_task():
    arrows = [">", "<"]
    num_trials,num_length ,correct = 5, 7, 0
    
    for i in range(num_trials):
        test_line = ""
        for i in range(num_length):
            arr = random.choice(arrows)
            test_line += arr
        print("This is the pattern:", test_line)
        
        start_time = time.time()
        user_input = input("input whether left or right:").strip().upper()
        end_time = time.time()
        tot_time = end_time - start_time
        
        if tot_time > given_time:
            print(f"Out of time for this round, used {tot_time} seconds the limit is {given_time}")
            continue

        if user_input == diction[test_line[len(test_line) // 2]]:
            
            print("Your answer was correct")
            print()
            correct += 1
        else:
            print("Wrong answer ")
            print()
            
    print(f"You answered {correct} / {num_trials}")
            
    



if __name__ == "__main__":
    arrow_task()