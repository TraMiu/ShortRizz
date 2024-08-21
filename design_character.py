from openai import OpenAI

client = OpenAI(api_key="sk-proj-EKcSHHzafepvFF5jcdc0T3BlbkFJ3x66vbhAgcfKOX2SnmMv")

def generate_structured_description(conversation_history, model="gpt-4o-mini"):
    """
    Generate a structured character description response from the AI model based on the conversation history.
    """
    response = client.chat.completions.create(
        model=model,
        messages=conversation_history,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content.strip()

def create_description_prompt():
    """
    Create the initial prompt for the character generator, which includes the example description.
    """
    return [
        {"role": "system", "content": "I am a famous character designer who writes character descriptions based on their key features."}
    ]

def add_user_message(conversation_history, key_feature, example, gender, age):
    """
    Append the user's message to the conversation history to specify the story setting or theme.
    """
    # if age == old turn switch gender from boy -> man, girl -> woman
    if age == "old":
        if gender == "boy":
            gender = "man"
        else:
            gender = "woman"
    conversation_history.append({"role": "user", "content": f"Give me a short description for character consistency for a {age} {gender} who {key_feature} in 50 words. Learn from this {example}. Be creative"})
    return conversation_history

def get_user_input():
    """
    Prompt the user to enter today's topic.
    """
    return input("Enter key feature: ")

example = "A little boy with short black hair and larget blue eyes, well structured nose and mouth, a red hoodie with skill symbol on the front, blue jeans and black loafer shoes"

# Example usage:
conversation_history = create_description_prompt()
print("Example character: ", example)
gender = input("boy/girl: ")
age = input("is little, young, or old:")
key_feature = get_user_input()
conversation_history = add_user_message(conversation_history, key_feature, example, gender, age)
character = generate_structured_description(conversation_history)

# write the generated story to txt file
with open('character.txt', 'w') as f:
    f.write(character)