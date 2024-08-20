from fpdf import FPDF
import pandas as pd

df = pd.read_csv()
pdf = FPDF(orientation="P", unit="mm", format="a4")

pdf.add_page()
pdf.output("output.pdf")