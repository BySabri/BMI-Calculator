import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=200)
window.config(bg="white",padx=10,pady=50)

name_label = tkinter.Label()
name_label.config(text="BMI Calculator",bg="white",fg="black",font=5,pady=10)
name_label.grid(row=0, column=2,)

window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=2)
window.columnconfigure(3, weight=1)

weight_label = tkinter.Label()
weight_label.config(text="Weight =",bg="white",fg="black",font=5)
weight_label.grid(row=1, column=1,pady=5)

weight_entry = tkinter.Entry()
weight_entry.config(width=23,bg="white",fg="black")
weight_entry.grid(row=1, column=2,pady=5)

weight_unit_label = tkinter.Label()
weight_unit_label.config(text="kg",bg="white",fg="black",font=5)
weight_unit_label.grid(row=1, column=3,pady=5)

height_label = tkinter.Label()
height_label.config(text="Height =",bg="white",fg="black",font=5)
height_label.grid(row=3, column=1,pady=5)

height_entry = tkinter.Entry()
height_entry.config(width=23,bg="white",fg="black")
height_entry.grid(row=3, column=2,pady=5)

height_unit_label = tkinter.Label()
height_unit_label.config(text="cm",bg="white",fg="black",font=5)
height_unit_label.grid(row=3, column=3,pady=5)

result = tkinter.Label()
result.grid(row=5, column=2,pady=5)
result.config(bg="white", fg="black", font=3)

def get_info():
    try:
        weight = int(weight_entry.get())
        height = int(height_entry.get())
        calculate = round(weight / ((height/100)**2),2)

        if calculate < 18.5:
            result.config(text=f"Your BMI is {calculate}\n You are under weight ")
            color = "#FFAF45"
        elif 18.5 <= calculate < 25:
            result.config(text=f"Your BMI is {calculate}\n You are normal ")
            color = "#90D26D"
        elif 25 <= calculate < 30:
            result.config(text=f"Your BMI is {calculate}\n You are overweight ")
            color = "#FFAF45"
        elif 30 <= calculate < 35:
            result.config(text=f"Your BMI is {calculate}\n You are obese ")
            color = "#FF204E"
        elif 35 <= calculate:
            result.config(text=f"Your BMI is {calculate}\n You are extremely obese ")
            color = "#FE0000"

        window.config(bg=color)
        name_label.config(bg=color)
        weight_label.config(bg=color)
        weight_unit_label.config(bg=color)
        height_label.config(bg=color)
        height_unit_label.config(bg=color)
        result.config(bg=color)

    except ValueError:
        result.config(text="Please enter a number")


calculate_button = tkinter.Button()
calculate_button.config(text="Calculate",command=get_info ,width=20,bg="white",border=(1))
calculate_button.grid(row=4, column=2,pady=5)




window.mainloop()