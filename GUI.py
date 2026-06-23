import tkinter as tk
from tkinter import ttk
#from cybersecurity_diagnostics import CyberSecurityDiagnostics


class CyberSecurityGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Consultant")

        #self.diagnostic_system = CyberSecurityDiagnostics()


        title = tk.Label(
            root,
            text="AI-Based Brute Force Detection Assistant",
            font=("Arial", 16, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=(12, 8))

        # ── Left panel frame 
        left = tk.Frame(root)
        left.grid(row=1, column=0, padx=(15, 8), pady=4, sticky="n")

        # Input Type
        ttk.Label(left, text="Input Type", font=("Arial", 10, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 2))
        self.input_type_var = tk.StringVar(value="IP Address")
        input_type_dropdown = ttk.Combobox(
            left,
            textvariable=self.input_type_var,
            values=["IP Address"],
            state="readonly",
            width=22
        )
        input_type_dropdown.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 10))

        # Evidence Variables label
        ttk.Label(left, text="Evidence Variables", font=("Arial", 10, "bold")).grid(
            row=2, column=0, columnspan=2, sticky="w", pady=(4, 6))

        evidence_vars = [
            ("Multiple failed",      "multiple_failed_var"),
            ("Same IP",              "same_ip_var"),
            ("Many accounts",        "many_accounts_var"),
            ("Outside hours",        "outside_hours_var"),
            ("Suspicious IP",        "suspicious_ip_var"),
            ("Success after failures","success_after_failures_var"),
        ]

        self.evidence_dropdowns = {}
        for i, (label, attr) in enumerate(evidence_vars):
            ttk.Label(left, text=label).grid(row=3 + i, column=0, sticky="w",
                                              padx=(0, 10), pady=4)
            var = tk.StringVar(value="NA")
            setattr(self, attr, var)
            cb = ttk.Combobox(
                left,
                textvariable=var,
                values=["NA", "True", "False"],
                state="readonly",
                width=10
            )
            cb.grid(row=3 + i, column=1, sticky="w", pady=4)
            self.evidence_dropdowns[attr] = cb

        # Analyze button
        analyze_button = ttk.Button(left, text="Analyze", command=self.run_analysis,
                                    width=22)
        analyze_button.grid(row=3 + len(evidence_vars), column=0, columnspan=2,
                            pady=(14, 4))

        self.textbox = tk.Text(root, height=22, width=48, wrap="word")
        self.textbox.grid(row=1, column=1, padx=(8, 15), pady=4, sticky="nsew")

        # Auto-size window to fit all widgets, then lock minimum size
        root.update_idletasks()
        w = root.winfo_reqwidth()
        h = root.winfo_reqheight()
        root.geometry(f"{w}x{h}")
        root.minsize(w, h)

    def run_analysis(self):
        result = self.diagnostic_system.analyze_threat(
            self.input_type_var.get(),
            self.target_var.get()
        )

        output_text = f"Target:\n{result['target']}\n\n"
        output_text += f"Diagnosis:\n{result['diagnosis']}\n\n"
        output_text += f"Threat Score:\n{result['threat_score']}%\n\n"
        output_text += f"Risk Level:\n{result['risk_level']}\n\n"
        output_text += f"Explanation:\n{result['explanation']}\n\n"
        output_text += "Recommended Actions:\n"

        for action in result["recommendations"]:
            output_text += f"- {action}\n"

        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, output_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = CyberSecurityGUI(root)
    root.mainloop()
