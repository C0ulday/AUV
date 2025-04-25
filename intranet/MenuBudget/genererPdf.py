import io
import os 
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from intranet.models import Facture,\
                            OperationFacture
from siteAUV.settings import BASE_DIR

def genererBufferFacture(idFacture):
    myFacture = Facture.objects.get(pk = idFacture)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    width, height = A4
    print(width,height)
    p = Canvas(buffer, pagesize = A4, bottomup=1)
    #Logo AUV
    p.drawImage(os.path.join(BASE_DIR, "siteAUV/static/img/logo_AUV.png"), 30, height - 90, width = 80, height = 80, preserveAspectRatio = True, mask='auto')
    #Références facture
    p.setFont("Helvetica-Bold", 12)
    p.drawString(width/2 + 30, height - 50, "Facture n° " + str(myFacture.code))
    p.drawString(width/2 + 30, height - 65, "Date : " + str(myFacture.date))
    #Adresse AUV
    p.setFont("Helvetica-Bold", 10)
    p.drawString(30, height - 110, "Aéro ULM Valence")
    p.setFont("Helvetica", 10)
    p.drawString(30, height - 125, "730 Chemin du vol à voile, Aéroport de Valence-Chabeuil")
    p.drawString(30, height - 140, "26120 Chabeuil, France")
    p.drawString(30, height - 155, "Tél : 06 66 65 23 39")
    p.drawString(30, height - 170, "Courriel : aero-ulm-valence@orange.fr")
    #Adresse Client
    p.rect(width/2 + 20 , height - 120 , width/2 - 50 , -80, stroke=1, fill=0)
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width/2 + 30, height - 140, str(myFacture.clientName) + " " + str(myFacture.clientVorname))
    p.setFont("Helvetica", 10)
    p.drawString(width/2 + 30, height - 155, str(myFacture.clientAdress))
    p.drawString(width/2 + 30, height - 170, str(myFacture.clientZip) + " " + str(myFacture.clientCity))
    p.drawString(width/2 + 30, height - 185, str(myFacture.clientCountry))
    #Opérations
    lines = [['Code', 'Objet', 'Prix unitaire HT', 'Quantité', 'Prix total HT', 'TVA']
             ]
    myFactureOp = OperationFacture.objects.filter(facture = myFacture)
    styleSheet = getSampleStyleSheet()
    for factureOp in myFactureOp:
        lines.append([factureOp.code, paragraph.Paragraph(factureOp.objet, styleSheet['BodyText']), str(factureOp.prixHT) + ' €', str(factureOp.nb), str(factureOp.prixTotalHT) + ' €', '0'])
    t = Table(lines)
    listStyle = TableStyle([('ALIGN',(2,1),(-1,-1),'RIGHT'),
                            ('VALIGN',(0,0), (-1,-1),'TOP'),
                             ('ALIGN',(0,0),(-1,0),'CENTER'),
                             ('GRID', (0,0), (-1,-1), 1, colors.black),
                             ('FONT', (0,0), (-1,0), 'Helvetica-Bold', 9),
                             ('FONT', (0,1), (-1,-1), 'Helvetica', 9),
                             ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                            ])
    t._argW[0]=40
    t._argW[1]=270
    t._argW[2]=80
    t._argW[3]=50
    t._argW[4]=70
    t._argW[5]=30
    t.setStyle(listStyle)
    t.wrapOn(p,width,height)
    t.drawOn(p,30 ,height - 500)
    #Montant total
    prixTotal = 0
    for factureOp in myFactureOp:
        prixTotal += factureOp.prixTotalHT
    p.drawString(30, height - 550, 'Mode de règlement : virement')
    p.drawString(30, height - 565, 'IBAN : FR76 1027 8089 1600 0205 0130 105')
    p.drawString(30, height - 580, 'Échéance : ' + str(myFacture.date.strftime("%d/%m/%Y")))
    p.setFont("Helvetica-Bold", 10)
    p.drawString(width/2 + 150, height - 580, 'Total TTC : ' + str(prixTotal) + ' €')
    #Facture acquitée
    print(myFacture.acquite.id)
    if myFacture.acquite.id == 2 :
        p.rotate(45)
        p.translate(100, -250)
        p.setFillColor(colors.red, alpha = 0.5)
        p.setFont("Helvetica-Bold", 26)
        p.drawString(150, height - 650, "Facture Acquittée")
        p.translate(-100, 250)
        p.rotate(-45)
        p.setFillColor(colors.black)
    #Signature Trésorier
    p.setFont("Helvetica-Oblique", 10)
    p.drawString(width - 150, height - 700, "Édité à Chabeuil")
    p.drawString(width - 150, height - 715, "Le " + str(myFacture.date.strftime("%d/%m/%Y")))
    p.drawString(width - 150, height - 730, "Le trésorier d'AUV")
    #ligne de séparation
    p.line(30, height-800, width-30, height-800)
    #Adresse AUV
    p.setFont("Helvetica-Oblique", 8)
    p.drawString(30, height - 820, "Aéro-ULM-Valence, Pôle Aviation Légère, 730 Chemin du Vol à Voile, 26120 Chabeuil - 06 66 65 23 39 - aero-ulm-valence@orange.fr")

    p.showPage()
    p.save()
    
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return buffer
    
