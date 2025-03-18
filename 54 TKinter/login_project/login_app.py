import customtkinter as tk


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login App")
        self.root.configure(bg="white")

        # Center window
        window_width = 720
        window_height = 480
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Configure grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Create frame
        self.frame = tk.CTkFrame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
        self.frame.grid(row=0, column=0)

        # Add widgets
        self.create_widgets()

    def create_widgets(self):
        # Title
        label = tk.CTkLabel(self.frame, text="Login", font=("Arial", 24))
        label.grid(row=0, column=0, columnspan=2, sticky="we", padx=10, pady=10)

        # User
        user_label = tk.CTkLabel(self.frame, text="User: ")
        user_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.user_entry = tk.CTkEntry(self.frame)
        self.user_entry.grid(row=1, column=1, sticky="we", padx=10, pady=10)

        # Password
        password_label = tk.CTkLabel(self.frame, text="Password: ")
        password_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.password_entry = tk.CTkEntry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1, sticky="we", padx=10, pady=10)

        # Button
        button = tk.CTkButton(self.frame, text="Login", command=self.validate_login)
        button.grid(row=3, column=0, columnspan=2, sticky="we", padx=10, pady=10)

    def validate_login(self):
        user = self.user_entry.get()
        password = self.password_entry.get()

        if user == "admin" and password == "admin":
            print("Login Success")
        else:
            print("Login Failed")


if __name__ == "__main__":
    window = tk.CTk()
    app = LoginApp(window)
    window.mainloop()
