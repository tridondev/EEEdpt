# Text_to_PPT

![image](https://img.shields.io/badge/-LangChain-32CD32?logo=LangChain&logoColor=white&style=for-the-badge)
![image](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)
![image](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)

This app uses artificial intelligence (AI) to generate PowerPoint presentations from a given topic. It is built using Streamlit, a Python framework for building web apps, and uses the following AI models:

GPT-3.5-turbo-instruct to generate slide titles

text-davinci-003 to generate slide content

To use the app, simply enter your topic and click the "Generate Presentation" button. The app will then generate a short PowerPoint presentation with 3 slides. The slides will be titled and formatted in a professional manner, and the content will be informative and engaging.

This app is a great tool for anyone who needs to create presentations quickly and easily. It is also a great way to learn about AI and how it can be used to automate tasks.

![Alt text](<Screenshot 2023-10-03 104745.png>)

Example PPT: [Large Language Models_presentation.pptx](https://github.com/AminHaghdadi/Text_to_PPT/files/12803059/Large.Language.Models_presentation.pptx)

## Deployment

To deploy this project run

1:
```bash
  git clone https://github.com/AminHaghdadi/Text_to_PPT.git
```
2: install requirements:
```bash
  pip install -r requirement.txt 
```
3:

Enter your OpenAI API in app.py 

4: Run in Terminal
```bash
streamlit run app.py
```
