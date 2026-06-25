# ==========================================
# 🌟 پروژه پیشرفته: بازی عدد شانس و مدیریت امتیازات 🌟
# 🌟 Advanced Lucky Number Game with Score Tracking 🌟
# ==========================================

import random
import time

def show_welcome_message():
    print("⚡ به بازی پیشرفته عدد شانس خوش آمدید! ⚡")
    print("=========================================")
    time.sleep(0.3)

def choose_difficulty():
    print("\n📊 لطفا سطح دشواری بازی را انتخاب کنید:")
    print("1. آسان (اعداد 1 تا 50 - 10 فرصت)")
    print("2. متوسط (اعداد 1 تا 100 - 7 فرصت)")
    print("3. سخت (اعداد 1 تا 200 - 5 فرصت)")
    
    while True:
        choice = input("گزینه مورد نظر (1/2/3): ").strip()
        if choice == "1":
            return 50, 10, "آسان"
        elif choice == "2":
            return 100, 7, "متوسط"
        elif choice == "3":
            return 200, 5, "سخت"
        print("❌ انتخاب نامعتبر است. لطفا 1، 2 یا 3 را وارد کنید.")

def play_round(max_number, max_attempts):
    secret_number = random.randint(1, max_number)
    attempts = 0
    
    print(f"\n🎯 من یک عدد بین 1 تا {max_number} انتخاب کردم. موفق باشید!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f" 🔢 حدس شماره {attempts + 1}: "))
        except ValueError:
            print(" ⚠️ لطفا یک عدد صحیح و معتبر وارد کنید!")
            continue
            
        attempts += 1
        
        if guess < secret_number:
            print(" 📈 عدد شانس بزرگتر است!")
        elif guess > secret_number:
            print(" 📉 عدد شانس کوچکتر است!")
        else:
            print(f" 🎉 تبریک! شما عدد {secret_number} را در {attempts} حرکت پیدا کردید! 🏆")
            score = (max_attempts - attempts + 1) * 10
            return True, score
            
    print(f" \n😢 فرصت شما تمام شد! عدد شانس من {secret_number} بود.")
    return False, 0

def main():
    show_welcome_message()
    total_score = 0
    rounds_played = 0
    
    while True:
        max_num, max_att, level_name = choose_difficulty()
        print(f"\n🚀 بازی در سطح {level_name} شروع می‌شود...")
        
        won, score = play_round(max_num, max_att)
        rounds_played += 1
        total_score += score
        
        print(f"\n📊 وضعیت شما -> دورهای بازی: {rounds_played} | امتیاز این دور: {score} | مجموع امتیازات: {total_score}")
        
        play_again = input("\n🔄 آیا می‌خواهید دوباره بازی کنید؟ (y/n): ").strip().lower()
        if play_again != 'y':
            print(f"\n👋 ممنون از بازی شما! مجموع امتیازات نهایی شما: {total_score} 🏁")
            break

if __name__ == "__main__":
    main()
