# ==========================================
# 🌟 پروژه کوچک: بازی حدس عدد شانس 🌟
# 🌟 Mini Project: Lucky Number Guessing Game 🌟
# ==========================================

import random
import time

def lucky_game():
    print("⚡ به بازی عدد شانس خوش آمدید! ⚡")
    print("---------------------------------")
    time.sleep(0.5)
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"من یک عدد بین 1 تا 100 انتخاب کردم. شما {max_attempts} فرصت دارید!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f" حدس شماره {attempts + 1}: "))
        except ValueError:
            print("❌ لطفاً یک عدد معتبر وارد کنید!")
            continue
            
        attempts += 1
        
        if guess < secret_number:
            print(" 📈 عدد بزرگتر است!")
        elif guess > secret_number:
            print(" 📉 عدد کوچکتر است!")
        else:
            print(f"🎉 تبریک! شما عدد {secret_number} را در {attempts} حرکت حدس زدید! 🏆")
            break
    else:
        print(f"😢 فرصت شما تمام شد! عدد شانس {secret_number} بود.")

if __name__ == "__main__":
    lucky_game()
