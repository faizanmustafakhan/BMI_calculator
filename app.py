import gradio as gr

# BMI Calculation Function
def calculate_bmi(weight, height):
    if height <= 0:
        return "⚠️ Height must be greater than 0"
    bmi = weight / (height ** 2)
    
    # BMI Category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return f"Your BMI is {bmi:.2f} → {category}"

# Gradio UI
demo = gr.Interface(
    fn=calculate_bmi,
    inputs=[
        gr.Number(label="Weight (kg)", value=70),
        gr.Number(label="Height (m)", value=1.75)
    ],
    outputs="text",
    title="⚕️ BMI Calculator",
    description="Enter your weight (kg) and height (m) to calculate your Body Mass Index."
)

if __name__ == "__main__":
    demo.launch()