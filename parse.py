from openai import OpenAI

client = OpenAI(api_key="sk-proj-EKcSHHzafepvFF5jcdc0T3BlbkFJ3x66vbhAgcfKOX2SnmMv")

def generate_structured_story(conversation_history, model="gpt-4o-mini"):
    """
    Generate a structured story response from the AI model based on the conversation history.
    """
    response = client.chat.completions.create(
        model=model,
        messages=conversation_history,
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content.strip()

def create_illustrator_prompt():
    """
    Create the initial prompt for the story generator, which includes an example story.
    """
    return [
        {"role": "system", "content": "I am a famouse illustrator who divides short stories into suitable phrases for illustration. Only return the dictionary with no empty lines in between."}]

def add_user_message(conversation_history, story):
    """
    Append the user's message to the conversation history to specify the story setting or theme.
    """
    conversation_history.append({"role": "user", "content": story + "For each phrase in the above story give a corresponding enhanced prompt to generate an illustration for the phrase and keep the main character name in the enhanced phrase. Return a dictionary of the exact phrase from the story and its enhanced prompt. The dictionary should have at least 15 members."})
    return conversation_history

with open('story.txt', 'r') as f:
    story = f.read()

# Example usage:
conversation_history = create_illustrator_prompt()
conversation_history = add_user_message(conversation_history, story)
dict = generate_structured_story(conversation_history)

# write the generated story to txt file
with open('scenes.txt', 'w') as f:
    f.write(dict)