import tkinter as tk
def on_click(button_value):
    current_text = entry_var.get()

    if button_value == 'C':
        entry_var.set('')
    elif button_value == '=':
        try:
            result = eval(current_text)
            entry_var.set(str(result))
        except:
            entry_var.set('Error')
    else:
        entry_var.set(current_text+button_value)

window = tk.Tk()
window.title('Basic calci')

entry_var = tk.StringVar()
entry = tk.Entry(window,textvariable=entry_var,font=("None",14))
entry.grid(row=0,column=0,columnspan=4,padx=8,pady=8)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window,text=button,padx=20,pady=20,font=("None",14),command=lambda btn=button:on_click(btn)).grid(row=row_val,column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
window.mainloop()
