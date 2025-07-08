import tkinter as tk
from tkinter import ttk, messagebox
from country_service import CountryService



class WorldUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Paises - World")
        self.service = CountryService()
        self._build_ui()
        self._load_country()

    def _build_ui(self):
        cols = ('Code', 'Name', 'Population', 'Capital', 'Poablación_Capital')
        self.tree = ttk.Treeview(self.root, columns=cols, show='headings')
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)

        frm = tk.Frame(self.root); frm.pack(pady=10)
        tk.Button(frm, text="Refrescar", command=self._load_country).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Añadir",    command=self._on_add).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Editar",    command=self._on_edit).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Eliminar",  command=self._on_delete).pack(side=tk.LEFT, padx=5)

    def _load_country(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for count in self.service.list_country():
            self.tree.insert('', tk.END, values=count)

    def _on_add(self):          
        def save_callback(data):
            self.service.add_country(data)
            self._load_country()
        self.CountryDialog(self.root, title="Añadir País", on_save=save_callback)

    def _on_edit(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Editar", "Seleccione un País")
            return
        data = self.tree.item(sel, 'values')
        messagebox.showinfo("Editar", f"Implementar edición de {data}")

    def _on_delete(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Eliminar", "Seleccione un cliente")
            return
        country_id = self.tree.item(sel, 'values')[0]
        if messagebox.askyesno("Eliminar", "¿Confirmar?"):
            self.service.remove_country(country_id)
            self._load_country()
    
    class CountryDialog(tk.Toplevel):
        def __init__(self, parent, title="Añadir/Editar País", country=None, on_save=None):
            super().__init__(parent)
            self.title(title)
            self.geometry("400x350")
            self.configure(bg="#ffffffed")
            self.result = None
            self.on_save = on_save

            labels = ["Código", "Nombre", "Población", "Capital", "Población Capital"]
            self.entries = {}

            for i, label in enumerate(labels):
                tk.Label(self, text=label, bg="#f1f8e9", fg="#000000", font=('Arial', 10, 'bold')).grid(row=i, column=0, padx=15, pady=10, sticky="e")
                entry = tk.Entry(self, font=('Arial', 10), bg="#ffffff", fg="#222")
                entry.grid(row=i, column=1, padx=15, pady=10)
                self.entries[label] = entry

            if country:
                for i, key in enumerate(labels):
                    self.entries[key].insert(0, country[i])

            btn_frame = tk.Frame(self, bg="#f1f8e9")
            btn_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)
            tk.Button(btn_frame, text="Guardar", bg="#00ff0dcc", fg="white", font=('Arial', 10, 'bold'),
                    command=self.on_save, width=10).pack(side=tk.LEFT, padx=10)
            tk.Button(btn_frame, text="Cancelar", bg="#b71c1c", fg="white", font=('Arial', 10, 'bold'),
                    command=self.destroy, width=10).pack(side=tk.LEFT, padx=10)

            self.grab_set()
            self.transient(parent)
            self.wait_window(self)
