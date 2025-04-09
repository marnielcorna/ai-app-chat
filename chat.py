def stream_chat(prompt: str, model: str, client, temperature=0.7, stream=True):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        stream=stream,
    )

    print("🤖 GPT Response:\n", end="", flush=True)

    if stream:
        for chunk in response:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
    else:
        print(response.choices[0].message.content)
