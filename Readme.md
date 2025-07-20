Excel/csv to VCard Converter

Easily convert contacts stored in an Excel (.xlsx) file into a .vcf (vCard) format using Python. 

✨ Features
✅ Converts Excel contact sheets to .vcf  
✅ Supports `Name`, `Phone number` and `Email` fields  
✅ Ideal for bulk import of contacts

excel-to-vcard-convertor/
│
├── convert_to_vcf.py         # Main Python script
├── contacts.xlsx             # Example input Excel file
├── contacts.vcf              # Output vCard file (after script runs)
├── env/                      # Virtual environment folder
└── requirements.txt          # List of dependencies



🧑‍💻 How to Use This ?

📌 Step 1: Clone the Repository

    git clone git@github.com:Gopiverse/excel-to-vcard-convertor.git
    cd excel-to-vcard-convertor

🛠️ Step 2: Set Up a Virtual Environment
   Create a virtual environment to keep things clean:

    python3 -m venv env
    source env/bin/activate

📦 Step 3: Install Dependencies
     Install the required Python packages:

    pip install -r requirements.txt

📁 Step 4: Prepare Your Excel File

  ✅ Your headers must be exactly:

    Name
    Phone number

🚀 Step 5: Run the Script

      python convert_to_vcf.py

📤 Step 6: Import the .vcf File


