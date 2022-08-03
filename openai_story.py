import os
import openai
import json

config = json.load(open("config.json"))
openai.api_key = config["open_ai_api_key"]

def get_openai_completion(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.9,
        max_tokens=70,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response

def get_story(prompt):
    text = get_openai_completion(prompt)["choices"][0]["text"]
    story = text[0:279]
    story = story.rsplit('.', 1)[0] + "."
    story = story.replace("\n\n", " ")
    story = story.replace("\n", " ")

    return story
