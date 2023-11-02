# PyPDF2: Una guida alle funzioni principali

PyPDF2 è una libreria Python utilizzata per leggere, scrivere e manipolare file PDF. Questo README offre una panoramica delle sue funzioni principali e delle operazioni più comuni che si possono eseguire con questa libreria.

## Funzioni Principali

### 1. Lettura di file PDF

```python
from PyPDF2 import PdfReader

# Aprire un PDF in modalità lettura binaria
with open("esempio.pdf", "rb") as file:
    reader = PdfReader(file)
    print(f"Numero di pagine: {reader.numPages}")
```


### 2. Scrittura di un nuovo file PDF
```python
from PyPDF2 import PdfWriter

writer = PdfWriter()
# Qui puoi aggiungere pagine o effettuare altre modifiche
with open("nuovo.pdf", "wb") as output_file:
    writer.write(output_file)
```

### 3. Estrazione di testo da una pagina
```python
from PyPDF2 import PdfReader

with open("esempio.pdf", "rb") as file:
    reader = PdfReader(file)
    page = reader.getPage(0)  # Ottieni la prima pagina
    print(page.extractText())
```


### 4. Unire più PDF insieme
```python
from PyPDF2 import PdfReader, PdfWriter

writer = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf"]:
    reader = PdfReader(pdf)
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        writer.addPage(page)

with open("uniti.pdf", "wb") as output:
    writer.write(output)
```



### 5. Ruotare pagina
```python
from PyPDF2 import PdfReader, PdfWriter

with open("esempio.pdf", "rb") as file:
    reader = PdfReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(90)  # Ruota di 90 gradi in senso orario

    writer = PdfWriter()
    writer.addPage(page)
    with open("ruotato.pdf", "wb") as output_file:
        writer.write(output_file)
```


## Funzioni utili avanzate

- **Ritaglio di una pagina**: Puoi ritagliare una pagina specificando una nuova `cropBox`.

- **Aggiungere una password**: Con PyPDF2 puoi proteggere i tuoi file PDF aggiungendo una password.

- **Decrittare un PDF**: Se hai un PDF protetto da password, puoi usarlo per rimuovere la protezione.

- **E altro**: La libreria offre molte altre funzioni utili, come la capacità di inserire pagine, eliminare pagine, e molto altro ancora.

## Risorse aggiuntive

- [Documentazione ufficiale](https://pythonhosted.org/PyPDF2/)
- [Github repository](https://github.com/mstamy2/PyPDF2)




```python

```
