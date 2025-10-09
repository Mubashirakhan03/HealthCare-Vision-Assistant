<h2><b>Overview</b></h2>
An AI-powered app called the "HealthCare Vision Assistant" uses image recognition to evaluate food, fruits, or beverages and offers tailored health recommendations based on the user's medical condition. To provide intelligent dietary recommendations, it integrates natural language processing and computer vision.

<h2><b>Objectives</b></h2>
This project uses AI-powered vision and natural language models to help users determine whether the foods they choose are in line with their health conditions.
Through the analysis of both textual and visual input, the system provides insightful information about health.

<h2><b>Features</b></h2>

Upload an image of food, fruit, or a drink for analysis.

Enter your current health condition or medical concern.

AI analyzes whether the uploaded item is suitable for your condition.

Provides detailed and reason-based health recommendations.

Simple web-based interface built using Streamlit.

<h2><b>Technologies Used</b></h2>

Python

Streamlit – for the user interface

LangChain – for prompt handling and retrieval-augmented generation

OpenAI GPT-4o – for text analysis and contextual reasoning

NVIDIA Vision Model (Llama 3.2 Vision-Instruct) – for image understanding

Chroma Vector Store – for document retrieval

PIL (Pillow) – for image handling

dotenv – for environment variable management


<h2><b>Project Structure</b></h2>

```bash
HealthCare-Vision-Assistant/
│
├── app.py                # Main Streamlit application
├── nim.py                # Script to test NVIDIA Vision API
├── prompt.py             # Contains the system prompt for analysis
├── var.env               # Environment file with API keys
├── health analyzer.mp4   # Demonstration video of the application
├── .gitignore            # Git ignore file
└── README.md             # Documentation file
```
<h2><b>Installation and Setup</b></h2>

<h2><b>1. Clone the Repository</b></h2>

<pre> 
git clone https://github.com/Mubashirakhan03/HealthCare-Vision-Assistant.git cd HealthCare-Vision-Assistant 
</pre>



<h2><b>2. Install Dependencies</b></h2>

<pre>
pip install -qU langchain-google-genai
pip install langchain google-cloud
pip install python-dotenv
pip install --upgrade --quiet langchain-nvidia-ai-endpoints
pip install langchain_openai
pip install -qU transformers langchain_openai langchain_chroma
pip install langchain_community
pip install streamlit
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu 
</pre>


<h2><b>3. Set Environment Variables</b></h2>
Create a .env or var.env file and include your API keys:

<pre>
OPENAI_API_KEY=your_openai_api_key
NVIDIA_API_KEY=your_nvidia_api_key
</pre>



<h2><b>How to Run</b></h2>
<h4><b>For the main application</b></h4>
<pre>
streamlit run app.py
</pre>
Open the local URL displayed in your terminal to access the application in your browser.




<h2><b>For NVIDIA Vision model testing</b></h2>
<pre>
python nim.py
</pre>


<h2><b>Usage</b></h2>
1. In the input field, enter your medical condition (for example, "I have diabetes").
2. Upload a picture of your food, drink, or fruit.
3. Click to proceed.
4. After analyzing the image, the system will provide detailed reasoning and advice on whether the item is appropriate for your condition.


<h2><b>Input</b></h2>
Health condition: “I have high blood pressure.”

Uploaded image: Banana


<h2><b>Output</b></h2>
People with high blood pressure can usually safely eat bananas. <br>
It has potassium, which aids in blood pressure regulation.  <br>
To maintain balanced sugar levels, portion control is recommended.


## Demo Video

You can watch the demo of the project here:  
👉 [Click to Watch the Video](https://github.com/Mubashirakhan03/HealthCare-Vision-Assistant/raw/main/health%20analyzer.mp4?raw=true)

<h2><b>Future Enhancements</b></h2>
Accuracy is increased through integration with a medical knowledge base.<br>
the choice to examine meal combinations rather than individual items.<br>
integration of chatbots and voice-based communication.<br>
Support for multiple languages to increase accessibility.

<h2><b>Author</b></h2>
Developed by <b>Mubashira Khan</b> <br>
This project was inspired by healthcare solutions that combine AI and computer vision to support better nutrition decisions.



<h2><b>Contact</b></h2>
For any queries: [mubashirakhan1001@gmail.com](mailto:mubashirakhan1001@gmail.com)
