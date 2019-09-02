#Module 'pyPdf', which helps in extracting the metadata from a pdf file. It contains the basic information regarding your actual data.

import pyPdf
def main():
            file_name = '/home/student/sample_pdf.pdf'
            pdfFile = pyPdf.PdfFileReader(file(file_name,'rb'))
            pdf_data = pdfFile.getDocumentInfo()
            print ("----Metadata of the file----")
            for md in pdf_data:
                        print (md+ ":" +pdf_data[md])
if __name__ == '__main__':
            main()
