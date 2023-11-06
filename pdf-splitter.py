import pikepdf

main_file = pikepdf.Pdf.open("wetransfer_pruebas_2023-10-24_1719/PRUEBA 1 - GESTION DE OPERACIONES - SEC. 5 - RODOLFO CARVAJAL V..PDF")

pages_per_doc = 24
num_docs = int(len(main_file.pages)/pages_per_doc)
print(f"{num_docs = }")



for i in range(num_docs):
    file_name = f"archivos-prueba1-GO/{i:0>{2}}-prueba1-GO-2023-2.pdf"
    new_file = pikepdf.Pdf.new()

    for p in range(pages_per_doc):
        page = i*pages_per_doc + p
        new_file.pages.append(main_file.pages[page])
        new_file.save(file_name)


    print(f"Saved {file_name}")


print(len(main_file.pages))
