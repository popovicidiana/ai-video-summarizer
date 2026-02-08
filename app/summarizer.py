import markdown
import textwrap

def summarize_transcript(client, transcript_text):

    # Split the text into chunks of roughly 8000 characters
    chunks = textwrap.wrap(transcript_text, width=8000, break_long_words=False)

    intermediate_summaries = []
    
    for chunk in chunks:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this section of a video transcript, preserving key points: \n\n{chunk}"
                }
            ],
            model="llama-3.1-8b-instant",
            temperature=0.3,
        )
        intermediate_summaries.append(response.choices[0].message.content)

    # Combine the mini-summaries into one final report
    combined_summary_text = "\n\n".join(intermediate_summaries)
    
    final_response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": (
                    "Below are summaries of different parts of a video. "
                    "Please synthesize them into a single, cohesive summary with bullet points:\n\n"
                    f"{combined_summary_text}"
                ),
            }
        ],
        model= "llama-3.3-70b-versatile",
        temperature=0.3,
    )

    html_content = markdown.markdown(
        final_response.choices[0].message.content
    )
    return html_content