import gradio as gr
from dotenv import load_dotenv
from src.deep_research import ResearchManager

load_dotenv(override=True)


async def run(query: str, num_items: int):
    count = 0
    async for chunk in ResearchManager().run(query):
        count += 1
        yield chunk
        if count >= num_items:
            break

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research Assistant")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    num_research = gr.Number(label="Number of Research items", value=3)
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=[query_textbox, num_research], outputs=report)
    query_textbox.submit(fn=run, inputs=[query_textbox, num_research], outputs=report)

ui.launch(inbrowser=True)
