import os
import tkinter as tk
from tkinter import ttk, messagebox
from dotenv import load_dotenv
from .database import SessionLocal, engine
from .models import Base, Note

load_dotenv()
APP_TITLE = os.getenv("APP_TITLE", "Demo Tkinter + SQLAlchemy + .env")

def init_db():
    Base.metadata.create_all(bind=engine)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("560x460")
        self._build_ui()
        self.load_notes()

    def _build_ui(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)

        ttk.Label(self, text="Titre").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.title_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.title_var).grid(row=0, column=1, padx=8, pady=8, sticky="ew")

        ttk.Label(self, text="Contenu").grid(row=1, column=0, padx=8, pady=8, sticky="nw")
        self.content_text = tk.Text(self, height=6)
        self.content_text.grid(row=1, column=1, padx=8, pady=8, sticky="nsew")

        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=2, column=1, sticky="e", padx=8, pady=4)
        ttk.Button(btn_frame, text="Enregistrer", command=self.save_note).pack(side="right", padx=4)
        ttk.Button(btn_frame, text="Actualiser", command=self.load_notes).pack(side="right", padx=4)

        ttk.Label(self, text="Notes").grid(row=3, column=0, padx=8, pady=(12,4), sticky="w")
        self.tree = ttk.Treeview(self, columns=("id", "title", "content", "created"), show="headings", height=8)
        for col, w in [("id", 40), ("title", 180), ("content", 240), ("created", 160)]:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=w, anchor="w")
        self.tree.grid(row=3, column=1, padx=8, pady=(4,8), sticky="nsew")

    def save_note(self):
        title = self.title_var.get().strip()
        content = self.content_text.get("1.0", "end").strip()
        if not title:
            messagebox.showwarning("Champ requis", "Titre manquant.")
            return
        with SessionLocal() as db:
            note = Note(title=title, content=content)
            db.add(note)
            db.commit()
        self.title_var.set("")
        self.content_text.delete("1.0", "end")
        self.load_notes()

    def load_notes(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        with SessionLocal() as db:
            for n in db.query(Note).order_by(Note.id.desc()).all():
                self.tree.insert("", "end", values=(n.id, n.title, n.content, n.created_at))