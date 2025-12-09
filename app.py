import gradio as gr

# ---------- Algorithm Logic ----------

def linear_search_steps(arr, target):
    steps = []
    for i, value in enumerate(arr):
        if value == target:
            steps.append(f"Step {i+1}: Compare target {target} with arr[{i}] = {value} → FOUND ✅")
            result = f"Result: Found {target} at index {i}.\n\n"
            return result + "\n".join(steps)
        else:
            steps.append(f"Step {i+1}: Compare target {target} with arr[{i}] = {value} → not equal ❌")

    result = f"Result: {target} was NOT found in the list.\n\n"
    return result + "\n".join(steps)


def run_linear_search(list_str, target_str):
    # Parse and validate list
    try:
        numbers = [int(x.strip()) for x in list_str.split(",") if x.strip() != ""]
    except ValueError:
        return "❗ Error: please enter only integers separated by commas, e.g. 4, 2, 7, 9, 1"

    if len(numbers) == 0:
        return "❗ Error: your list is empty. Please enter at least one number."

    # Parse and validate target
    try:
        target = int(target_str.strip())
    except ValueError:
        return "❗ Error: target must be a single integer, e.g. 7"

    return linear_search_steps(numbers, target)


# ---------- Gradio UI ----------

with gr.Blocks(title="Linear Search Simulator") as demo:
    gr.Markdown(
        """
        # Linear Search Simulator

        Enter a list of integers and a target value.  
        This app will run **linear search** and show each comparison step.
        """
    )

    with gr.Row():
        list_input = gr.Textbox(
            label="List of numbers (comma-separated)",
            placeholder="Example: 4, 2, 7, 9, 1"
        )
        target_input = gr.Textbox(
            label="Target number",
            placeholder="Example: 7"
        )

    run_button = gr.Button("Run Linear Search")

    output_box = gr.Markdown(label="Search Steps & Result")

    run_button.click(
        fn=run_linear_search,
        inputs=[list_input, target_input],
        outputs=output_box
    )

if __name__ == "__main__":
    demo.launch()