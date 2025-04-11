
def stream_chat(messages: list, model: str, client, temperature=0.7):
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=True
    )

    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            # For flushing message, uncomment this line and remove printing from interactive_chat.process_input():
            # print(content, end="", flush=True)
            full_response += content

    print()
    return full_response
