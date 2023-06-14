import tkinter as tk

window = tk.Tk()
window.title("Quadratic")
window.geometry("300x300")

tk.Label(text= "Parameter a:").pack()
a_in = tk.Entry()
a_in.pack()

tk.Label(text= "Parameter b:").pack()
b_in = tk.Entry()
b_in.pack()

tk.Label(text= "Parameter c:").pack()
c_in = tk.Entry()
c_in.pack()



def compute():
  global a_in
  global b_in
  global c_in

  a = int(a_in.get())
  b = int(b_in.get())
  c = int(c_in.get())

  if b**2 > 4*a*c:
    root1 = round((- b - (b**2 - 4*a*c)**(1/2))/2/a, 2)
    root2 = round((- b + (b**2 - 4*a*c)**(1/2))/2/a, 2)
    label.configure(text= f"The roots are {root1} and {root2}.")
  elif b**2 == 4*a*c:
    label.configure(text= f"The root is {round( - b/2/a, 2)}.")
  else:
    label.configure(text= "This equation doesn't have real roots.")
  
button = tk.Button(text= "Compute equation", command= compute).pack()

label = tk.Label(text= "The results will be printed here.")
label.configure()
label.pack()

tk.mainloop()
