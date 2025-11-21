from .gui import App, init_db

def main():
    init_db()
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()