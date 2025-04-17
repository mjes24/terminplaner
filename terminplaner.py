import datetime

termine = {
    "2025-08-01": "Vertragsstart Ausbildung",
    "2025-08-15": "Feedbackrunde",
    "2025-09-01": "1. Projektbesprechung"
}

heute = datetime.date.today().strftime("%Y-%m-%d")

if heute in termine:
    print(f"Erinnerung: Heute steht an – {termine[heute]}")
else:
    print("Heute gibt es keinen Termin.")
