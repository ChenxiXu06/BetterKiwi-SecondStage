from openai import OpenAI

client = OpenAI(api_key = "Your OpenAI API")  # Due to requirements, API can not be presented. You should use your own OpenAI API
topic = input("Enter the data structure topic you want to be tested on >>> ")

history = [
    {"role": "system", "content": "You are a very tedious teacher and computer scientist who loves giving very complicated and confusing multiple choice questions to students for a quiz. Ask the user for the topics they want to be tested on."},
    {"role": "user", "content": f"I want a quiz on {topic}, provide me with exactly one nasty and confusing question. And provide me with the COT chain of thought of why you generate the question like this"}
]

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=history
)

print(response.choices[0].message.content)

history.append({"role": "assistant", "content": response.choices[0].message.content})
history.append({"role": "system", "content": "You should generate every question like the COT process"})

question = 1
with open('questions.txt', 'w') as outfile_1, open('ratings.txt', 'w') as outfile_2:
    while question <= 2:
        history.append({"role": "user", "content": f"generate a question on the {topic}"})
        
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=history
        )

        question_text = response.choices[0].message.content.strip()
        print(f"Question {question}: {question_text}\n")
        outfile_1.write(f"{question}: {question_text}\n\n")

        history.append({"role": "assistant", "content": question_text})
        history.append({"role": "user", "content": "Give me a rating of one to five for the question you've generated. Be objective. I only need a number as output."})

        rating_response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=history
        )
        rating = rating_response.choices[0].message.content.strip()
        print(f"Rating: {rating}\n")
        outfile_2.write(f"Rating {question}: {rating}\n")

        history.append({"role": "assistant", "content": rating})
        question += 1
