from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


PAGE_MARGIN_X = 50
TOP_MARGIN = 50
BOTTOM_MARGIN = 50
LINE_HEIGHT = 15


def _check_page_space(c, y, height):
    """
    Checks if there's space left on the page.
    Creates a new page if required.
    Returns updated y position.
    """
    if y < BOTTOM_MARGIN:
        c.showPage()
        c.setFont("Helvetica", 10)
        return height - TOP_MARGIN
    return y


def generate_pdf(analysis_result, output_path, dataset_name="Uploaded Dataset"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    y = height - TOP_MARGIN

    # -------- Title --------
    c.setFont("Helvetica-Bold", 18)
    c.drawString(PAGE_MARGIN_X, y, "Chemical Equipment Summary Report")

    y -= 30
    c.setFont("Helvetica", 10)
    c.drawString(PAGE_MARGIN_X, y, f"Dataset: {dataset_name}")

    # -------- Summary Section --------
    y -= 40
    y = _check_page_space(c, y, height)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(PAGE_MARGIN_X, y, "Summary Statistics")

    y -= 20
    c.setFont("Helvetica", 10)

    summary = analysis_result["summary"]
    for key, value in summary.items():
        y = _check_page_space(c, y, height)
        label = key.replace("_", " ").title()
        c.drawString(PAGE_MARGIN_X + 10, y, f"{label}: {round(value, 2)}")
        y -= LINE_HEIGHT

    # -------- Type Distribution --------
    y -= 25
    y = _check_page_space(c, y, height)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(PAGE_MARGIN_X, y, "Equipment Type Distribution")

    y -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(PAGE_MARGIN_X + 10, y, "Type")
    c.drawString(PAGE_MARGIN_X + 200, y, "Count")

    y -= LINE_HEIGHT
    c.setFont("Helvetica", 10)

    count_by_type = analysis_result["count_distribution"]["count_by_type"]
    for eq_type, count in count_by_type.items():
        y = _check_page_space(c, y, height)
        c.drawString(PAGE_MARGIN_X + 10, y, str(eq_type))
        c.drawString(PAGE_MARGIN_X + 200, y, str(count))
        y -= LINE_HEIGHT

    # -------- Averages by Type --------
    y -= 30
    y = _check_page_space(c, y, height)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(PAGE_MARGIN_X, y, "Average Parameters by Equipment Type")

    y -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(PAGE_MARGIN_X + 10, y, "Type")
    c.drawString(PAGE_MARGIN_X + 120, y, "Flowrate")
    c.drawString(PAGE_MARGIN_X + 220, y, "Pressure")
    c.drawString(PAGE_MARGIN_X + 320, y, "Temperature")

    y -= LINE_HEIGHT
    c.setFont("Helvetica", 10)

    avg_flow = analysis_result["count_distribution"]["average_flowrate_by_type"]
    avg_pressure = analysis_result["count_distribution"]["average_pressure_by_type"]
    avg_temp = analysis_result["count_distribution"]["average_temperature_by_type"]

    for eq_type in avg_flow.keys():
        y = _check_page_space(c, y, height)
        c.drawString(PAGE_MARGIN_X + 10, y, str(eq_type))
        c.drawString(PAGE_MARGIN_X + 120, y, f"{round(avg_flow[eq_type], 2)}")
        c.drawString(PAGE_MARGIN_X + 220, y, f"{round(avg_pressure[eq_type], 2)}")
        c.drawString(PAGE_MARGIN_X + 320, y, f"{round(avg_temp[eq_type], 2)}")
        y -= LINE_HEIGHT

    # -------- Footer --------
    c.setFont("Helvetica", 9)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.drawRightString(
        width - PAGE_MARGIN_X,
        BOTTOM_MARGIN - 15,
        f"Generated on: {timestamp}"
    )

    c.showPage()
    c.save()
