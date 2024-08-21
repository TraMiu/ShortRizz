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
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content.strip()

def create_story_prompt():
    """
    Create the initial prompt for the story generator, which includes the example story.
    """
    return [
        {"role": "system", "content": "I am a famous writer who writes short stories that teach readers about moral lessons. I printout stories with no lines in between"},
        {"role": "user", "content": "Would you like to change the example story? (yes/no)"}
    ]

def add_user_message(conversation_history, topic, example_story):
    """
    Append the user's message to the conversation history to specify the story setting or theme.
    """
    conversation_history.append({"role": "user", "content": "Generate a story about 150 words to teach reader a lesson:" + topic + "Learn from this example story: " + example_story})
    return conversation_history

def get_user_input():
    """
    Prompt the user to enter today's topic.
    """
    return input("Enter today's topic: ")

example_story = "Nahtan was a cheerful boy who loved playing with his friends. However, there were some people around him who were always negative. At school, Nathan often heard negative comments from classmates who were constantly complaining. Nathan felt upset by the negativity, but his teacher noticed and wanted to help him. The teacher showed Nathan how he could choose to focus on positive things instead of letting negative comments bring him down. Nathan decided to ignore the negative comments and instead focus on the fun activities he enjoyed with his friends. Soon, he felt much happier and more confident. With his new attitude, Nathan found that he could spread positivity to others as well. He learned that his happiness is something he could control and share. Nathan discovered that focusing on the positive and spreading joy can make a difference. Remember, you can always choose to brighten your world and help others do the same."

# Example usage:
conversation_history = create_story_prompt()
print("Example story: ", example_story)
change_example_story = input("Would you like to change the example story? (y/n): ")
if change_example_story.lower() == "y":
    example_story = input("Enter the new example story: ")
topic = get_user_input()
conversation_history = add_user_message(conversation_history, topic, example_story)
story = generate_structured_story(conversation_history)

# write the generated story to txt file
with open('story.txt', 'w') as f:
    f.write(story)