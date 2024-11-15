import openai
import os
from dotenv import load_dotenv
from tkinter import Tk, Text, Button, Label, END

# Load the OpenAI API key from the .env file
load_dotenv()
openai.api_key = "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"

if not openai.api_key:
    raise ValueError("API Key not found. Ensure your .env file is configured correctly.")

# Function to send a prompt to OpenAI and display the response
def get_response():
    # Get the prompt from the input text box
    prompt = input_text.get("1.0", END).strip()
    if not prompt:
        output_text.delete("1.0", END)
        output_text.insert("1.0", "Please enter a prompt!")
        return

    try:
        # Make a request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use GPT-3.5-turbo model
            messages=[{"role": "user", "content": prompt}]
        )
        # Extract the assistant's reply
        reply = response['choices'][0]['message']['content'].strip()

        # Display the reply in the output text box
        output_text.delete("1.0", END)
        output_text.insert("1.0", reply)
    except Exception as e:
        # Handle errors and display them
        output_text.delete("1.0", END)
        output_text.insert("1.0", f"Error: {e}")

# Create the GUI window
root = Tk()
root.title("OpenAI Prompt Responder")
root.geometry("600x400")

# Add input label
input_label = Label(root, text="Enter your prompt:", font=("Arial", 12))
input_label.pack(pady=5)

# Add input text box for the user's prompt
input_text = Text(root, height=6, width=70, wrap="word", font=("Arial", 12))
input_text.pack(pady=5)

# Add submit button
submit_button = Button(root, text="Submit", command=get_response, font=("Arial", 12))
submit_button.pack(pady=10)

# Add output label
output_label = Label(root, text="AI's response:", font=("Arial", 12))
output_label.pack(pady=5)

# Add output text box for the AI's response
output_text = Text(root, height=10, width=70, wrap="word", font=("Arial", 12), bg="#f0f0f0")
output_text.pack(pady=5)

# Run the GUI event loop
root.mainloop()
