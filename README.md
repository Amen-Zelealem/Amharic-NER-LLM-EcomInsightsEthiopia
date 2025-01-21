# 🛒 **Amharic-NER-LLM-EcomInsightsEthiopia**
A comprehensive repository dedicated to **extracting insights** and **data** from Telegram channels, aimed at **optimizing** the e-commerce landscape in Ethiopia.

### 🔍 **Overview**
This repository serves as a framework for leveraging **Named Entity Recognition (NER)** in the Amharic language, specifically tailored for e-commerce applications.

## Selected Channels
The following Ethiopian-based Telegram e-commerce channels have been selected for data ingestion:
- **@ethio_brand_collection**

## 📂 **Project Structure**

```
+---.github
| └── workflows
| └── blank.yml
+---.vscode
| └── settings.json
+---notebooks
| ├── data_processing.ipynb
| ├── Fine_Tunning.ipynb
| ├── init.ipynb
| └── README.md
+---scripts
| ├── data_labeler.py
| ├── data_preprocessor.py
| ├── data_scrapper.py
| ├── init.py
| └── README.md
+---src
| └── README.md
| └── init.py
+---tests
| ├── README.md
| └── init.py
| └── test_data_labeler.py
| └── test_data_preprocessing.py
| └──test_data_scrapper.py
| ├── .gitignore
| ├── labeled_data_conll.conll
| ├── README.md
| └── requirements.txt
```

## 🛠️ Tools and Libraries
- **Python**: The primary programming language used for the implementation.
- **Telethon**: A Python library for interacting with Telegram’s API to scrape messages.
- **Pandas**: For data manipulation and storage in structured formats.
- **NLTK or SpaCy**: For text preprocessing and tokenization specific to Amharic linguistic features.

## 🚀 Installation Instructions
To run the project locally, follow these steps:

Clone the Repository:
`git clone https://github.com/Amen-Zelealem/Amharic-NER-LLM-EcomInsightsEthiopia.git`


`cd Amharic-NER-LLM-EcomInsightsEthiopia`

Set up the Virtual Environment:

`python3 -m venv .venv`
`source .venv/bin/activate  # For Windows: .venv\Scripts\activate`

Install Dependencies:

`pip install -r requirements.txt`


## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
   
2. Create a new branch: 
   
```git checkout -b feature-branch```  

3. Make your changes and commit: 

```git commit -m 'Add new feature'```
  
4. Push to the branch:
 
```git push origin feature-branch```

5. Open a pull request.

Feel free to reach out using the contact below:

✉️ [Amen-Zelealem](mailto:amenzelealem@gmail.com)

# **🌟 Elevate Your E-commerce Insights with Real-Time Intelligence!**
