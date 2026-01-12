import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "./best"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
model.to("mps")


def process_words(
    word1: str,
    word2: str,
    word3: str,
    temperature: float,
    top_p: float,
    max_new_token: int,
    no_repeat_ngram_size: int,
    do_sample: bool,
) -> str | None:
    prompt = f"Words: {word1}, {word2}, {word3}\nPoem:\n"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    best_poem = None
    best_score = -1
    for i in range(8):
        output = model.generate(
            **inputs,
            max_new_tokens=max_new_token,
            do_sample=do_sample,
            temperature=temperature,
            no_repeat_ngram_size=no_repeat_ngram_size,
            top_p=top_p,
        )

        poem = tokenizer.decode(output[0], skip_special_tokens=True).split("Poem:\n")[1]

        if best_poem is None:
            best_poem = poem

        score = 0
        if "\n" in poem:
            score += 1 if word1.lower() in poem.lower() else 0
            score += 1 if word2.lower() in poem.lower() else 0
            score += 1 if word3.lower() in poem.lower() else 0

            if score > best_score:
                best_poem = poem
                best_score = score

    return best_poem


with gr.Blocks(
    css="""
#orange-btn {
    background-color: orange;
}
""",
) as demo:
    gr.Markdown("## Poem Generator")

    w1 = gr.Textbox(label="Word 1")
    w2 = gr.Textbox(label="Word 2")
    w3 = gr.Textbox(label="Word 3")

    with gr.Accordion("Advanced settings", open=False):
        temperature = gr.Slider(0, 1, step=0.1, label="Temperature", value=0.8)
        top_p = gr.Slider(0, 1, step=0.1, label="Top p", value=1.0)
        max_len = gr.Slider(0, 200, step=10, label="Maximum length", value=50)
        no_repeat_ngram_size = gr.Slider(0, 5, step=1, label="No repeat ngram size", value=0)
        do_sample = gr.Checkbox(value=True, label="Do sample")

    btn = gr.Button("Generate", elem_id="orange-btn")

    output = gr.Textbox(label="Poem", lines=20)

    btn.click(
        fn=process_words,
        inputs=[w1, w2, w3, temperature, top_p, max_len, no_repeat_ngram_size, do_sample],
        outputs=output,
    )

demo.launch()
