from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    # Set Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 200)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="l",
            ln=1)
    pdf.line(10, 20, 200, 20)

    pdf.ln(260)
    # Set Footer
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(270)

        # Set footer for other pages
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")


pdf.output("output.pdf")
