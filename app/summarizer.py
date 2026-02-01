import markdown
import groq

def summarize_transcript(client, transcript_text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (
                    "Summarize the video transcript below into bullet points:\n\n"
                    f"{transcript_text}"
                ),
            }
        ],
        model= "llama-3.1-8b-instant",
        temperature=0.3,
    )

    html_content = markdown.markdown(
        chat_completion.choices[0].message.content
    )
    return html_content