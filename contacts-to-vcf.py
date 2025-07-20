import pandas as pd

# Load your Excelfile
userFile = pd.read_excel("ISTE Execom details 2025 (Responses).xlsx")  # change the filename as required

#for csv file use the code given below
#userFile = pd.read_csv("filename.csv")


# Create VCF content from xlsx file
vcf_lines = []
for i in range(len(userFile)):
    name = userFile.loc[i, 'Name']
    phone = userFile.loc[i, 'Phone number']

    vcf = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
END:VCARD
"""
    vcf_lines.append(vcf)

#Save to .vcf file and generate a .vcf file
with open("contacts.vcf", "w", encoding="utf-8") as f:
    f.writelines(vcf_lines)
print("VCF file created successfully.")
