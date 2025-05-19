import BST,csv
import tkinter as tk
from tkinter import messagebox

a=BST.BinarySearchTree()
root1=a.contruct_bst_from_csv()
def close(root1):
    root1.destroy()
    a.store_bst_data_to_csv()

def main():
    root=tk.Tk()
    root.title("Student Login")
    root.geometry("970x666")
    
    welcome_label = tk.Label(root, text="Welcome to DSA inc.", font=("Helvetica", 20))
    welcome_label.place(relx=0.5, rely=0.2, anchor='center')

    Students_btn = tk.Button(root, text="Student record", command=display_details,height=5,width=12)
    Students_btn.grid(row=1,column=1,padx=10,pady=10)
    Students_btn.place(relx=0.5, rely=0.4, anchor='center')

    Student_btn = tk.Button(root, text="Student", command=logs,height=5,width=12)
    Student_btn.grid(row=2,column=1,padx=10,pady=10)
    Student_btn.place(relx=0.5, rely=0.5, anchor='center')

    createacc_btn= tk.Button(root, text="Create account", command=close,height=5,width=12)
    Student_btn.grid(row=3,column=1,padx=10,pady=10)
    Student_btn.place(relx=0.5, rely=0.6, anchor='center')
    
def display_details():
    try:
        rows = []
        with open("data.csv", 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rows.append(row)
        
        if rows:
            students_window = tk.Toplevel()
            students_window.title("All Details")
            label_frame = tk.LabelFrame(students_window, text="All Details")
            label_frame.pack(padx=10, pady=10)
            headers = ["ID", "Name", "Passkey"]
            for i, header in enumerate(headers):
                header_label = tk.Label(label_frame, text=header, font=("Arial", 10, "bold"))
                header_label.grid(row=0, column=i, padx=5, pady=5)
            for row_index, student in enumerate(rows, start=1):
                for col_index, detail in enumerate(student):
                    detail_label = tk.Label(label_frame, text=detail, font=("Arial", 10))
                    detail_label.grid(row=row_index, column=col_index, padx=5, pady=5)
        else:
            messagebox.showinfo("No Employee", "No Employee in CSV details")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The CSV file 'data.csv' does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
def logs():
    '''def login():
        employeeid = int(employee_id_entry.get())
        password = password_entry.get()
        b=check_employee_login(employeeid, password)
        s=a.search_name((int(employeeid),password))
        if b:
            messagebox.showinfo("Login Successful", "Welcome, " + s[1] + "!")
            close(root1)

        else:
            messagebox.showerror("Login Failed", "Invalid student ID or password.")
        '''
    def login():
        employeeid = int(employee_id_entry.get())
        password = password_entry.get()
        
        if check_employee_login(employeeid, password):
    
            employee_info = a.search_name(employeeid, password)
            if employee_info:
                messagebox.showinfo("Login Successful", "Welcome, " + employee_info.name + "!")
                root1.destroy()
            else:
                messagebox.showerror("Login Failed", "Invalid employee ID or password.")
        else:
            messagebox.showerror("Login Failed", "Invalid employee ID or password.")
    root1 = tk.Toplevel()
    root1.title("Employee Login")
    root1.geometry("344x333")

    employee_id_label = tk.Label(root1, text="Employee ID:")
    employee_id_label.grid(row=0, column=0, padx=10, pady=5)
    employee_id_entry = tk.Entry(root1)
    employee_id_entry.grid(row=0, column=1, padx=10, pady=5)
    
    
    password_label = tk.Label(root1, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(root1, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)
    
    
    login_button = tk.Button(root1, text="Login", command=login)
    login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    createacc_button = tk.Button(root1, text="Create Account", command=acc_creation)
    createacc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    deleteacc_button=tk.Button(root1, text="Delete Account", command=acc_deletion)
    deleteacc_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def check_employee_login(employeeid, password):
    if a.search_name(int(employeeid),password)is not None:
        return True
    else:
        return False

def acc_creation():
    def create_acc():
        if employee_id_entry.get().isalpha():
            messagebox.showerror("Error", "Id should be only numeric")
        a.insert(int(employee_id_entry.get()),name_entry.get(),password_entry.get())
        messagebox.showinfo("Success", "Account created sucessfully")
        close(root1)
    root1 = tk.Toplevel()
    root1.title("Employee Login")
    root1.geometry("344x333")

    employee_id_label = tk.Label(root1, text="Employee ID:")
    employee_id_label.grid(row=0, column=0, padx=10, pady=5)
    employee_id_entry = tk.Entry(root1)
    employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

    name_label = tk.Label(root1, text="Name:")
    name_label.grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root1)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    
    password_label = tk.Label(root1, text="Password:")
    password_label.grid(row=2, column=0, padx=10, pady=5)
    password_entry = tk.Entry(root1, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    Create_button = tk.Button(root1, text="Create Account", command=create_acc)
    Create_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


def acc_deletion():
    def delete_acc():
        if employee_id_entry.get().isalpha():
            messagebox.showerror("Error", "Id should be only numeric")
        a.delete(int(employee_id_entry.get()),password_entry.get())
        messagebox.showinfo("Success", "Account created sucessfully")
        close(root1)
        
    root1 = tk.Toplevel()
    root1.title("Employee Login")
    root1.geometry("344x333")

    employee_id_label = tk.Label(root1, text="Employee ID:")
    employee_id_label.grid(row=0, column=0, padx=10, pady=5)
    employee_id_entry = tk.Entry(root1)
    employee_id_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(root1, text="Password:")
    password_label.grid(row=2, column=0, padx=10, pady=5)
    password_entry = tk.Entry(root1, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    
    delete_button = tk.Button(root1, text="Delete Account", command=delete_acc)
    delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


    
main()
