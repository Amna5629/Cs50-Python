from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set the font for the header text
        self.set_font("helvetica", "", 48)
        # Move down 30 units from the top
        self.ln(30)
        # Centered title
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        # Add a line break
        self.ln(20)
        # Insert the image below the title
        self.image("./shirtificate.png", x=10, y=70, w=190)


def main():
    name = input("Name: ")
    shirt(name)


def shirt(s):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    # Adjusting the position to align the text on the shirt
    pdf.set_y(150)
    pdf.cell(0, 10, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
