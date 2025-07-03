# print("Kaun Banega Crorepati".center(50))
# name = input("Enter your name: ")
# print("Hello", name, "Welcome to Kaun Banega Crorepati.")
# print("Press Enter to Get Details of Instructions.")
# input()

# print("Read the Instructions Given Below Carefully")
# print('''
# (1) 🎮 Game Format:
# Total Questions: 15 multiple-choice questions.
# ...
# Safe Milestones:
# Q5: ₹10,000 (guaranteed)
# Q10: ₹3,20,000 (guaranteed)
# ''')

# print('''
# (3)✅ How to Play:
# Choose the Answer: You must choose one option.
# Wrong Answer: You lose and take home the last milestone amount.
# ''')

# print('''
# (3)🧰 Lifelines Available:
# 50:50 – Two incorrect options are removed.
# Audience Poll – You see the percentage of what the audience chose.
# ''')

# input("👉 Press Enter to start the KBC Game...")

# # Q1
# print("Question Number One is on your Screen :-")
# Que1 = ["Q1. Who was the first President of independent India?",
#         "Mahatma Gandhi", "Jawaharlal Nehru", "Rajendra Prasad", "Sardar Patel"]

# print(Que1[0])
# print("a)", Que1[1])
# print("b)", Que1[2])
# print("c)", Que1[3])
# print("d)", Que1[4])

# try:
#     e = input("Enter Your option (a/b/c/d):- ").lower()
#     if e == "c":
#         print("✅ You are absolutely correct")
#         print("Congratulations you have just won ₹1000")
#     else:
#         print("❌ Sorry, That was incorrect")
#         print("💔 Game Over")
#         exit()
# except:
#     print("⚠️ Invalid input. Game crashed.")
#     exit()

# # Q2
# print("Question Number Two is on your Screen :-")
# input("This question will be for ₹2000. Press Enter when ready.")
# print("Q2. Which planet is known as the Red Planet?")
# print("a) Earth")
# print("b) Mars")
# print("c) Jupiter")
# print("d) Saturn")

# try:
#     e = input("Enter Your option (a/b/c/d):- ").lower()
#     if e == "b":
#         print("✅ You are absolutely correct")
#         print("Congratulations you have just won ₹2000")
#     else:
#         print("❌ Sorry, That was incorrect")
#         print("💔 Game Over")
#         exit()
# except:
#     print("⚠️ Invalid input.")
#     exit()

# # Q3
# print("Question Number Three is on your Screen :-")
# print("Q3. Which is the national animal of India?")
# print("a) Lion")
# print("b) Tiger")
# print("c) Elephant")
# print("d) Leopard")

# try:
#     e = input("Enter Your option (a/b/c/d):- ").lower()
#     if e == "b":
#         print("✅ You are absolutely correct")
#         print("Congratulations you have just won ₹3000")
#     else:
#         print("❌ Sorry, That was incorrect")
#         print("💔 Game Over")
#         exit()
# except:
#     print("⚠️ Invalid input.")
#     exit()

# # Q4
# print("Question Number Four is on your Screen :-")
# print("Q4. Who wrote the Indian National Anthem?")
# print("a) Rabindranath Tagore")
# print("b) Bankim Chandra Chatterjee")
# print("c) Subhash Chandra Bose")
# print("d) Mahatma Gandhi")

# try:
#     e = input("Enter Your option (a/b/c/d):- ").lower()
#     if e == "a":
#         print("✅ You are absolutely correct")
#         print("Congratulations you have just won ₹5000")
#     else:
#         print("❌ Sorry, That was incorrect")
#         print("💔 Game Over")
#         exit()
# except:
#     print("⚠️ Invalid input.")
#     exit()

# # Q5 – Milestone
# print("Question Number Five is on your Screen :-")
# print("Q5. What is the capital of Australia?")
# print("a) Sydney")
# print("b) Melbourne")
# print("c) Canberra")
# print("d) Perth")

# try:
#     e = input("Enter Your option (a/b/c/d):- ").lower()
#     if e == "c":
#         print("✅ You are absolutely correct")
#         print("🎉 Congratulations, you've reached your first milestone!")
#         print("💰 You have won ₹10,000 guaranteed!")
#     else:
#         print("❌ Sorry, That was incorrect")
#         print("💔 Game Over")
#         print("💸 You take home ₹0")
#         exit()
# except:
#     print("⚠️ Invalid input.")
#     exit()